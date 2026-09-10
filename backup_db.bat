@echo off
echo ============================================
echo  Alto Gas SPA - Respaldo de Base de Datos
echo ============================================

REM Lee BACKUP_DATABASE_URL desde .env (archivo ignorado por git)
set "DATABASE_URL="
for /f "usebackq tokens=1,* delims==" %%A in (".env") do (
    if /i "%%A"=="BACKUP_DATABASE_URL" set "DATABASE_URL=%%B"
)

if not defined DATABASE_URL (
    echo.
    echo [ERROR] No se encontro BACKUP_DATABASE_URL en el archivo .env
    echo.
    echo Copia la variable DATABASE_URL del servicio Postgres en Railway
    echo y agregala al final de .env con este formato:
    echo.
    echo   BACKUP_DATABASE_URL=postgresql://usuario:clave@host:puerto/railway
    echo.
    pause
    exit /b 1
)

if not exist backups mkdir backups

REM Timestamp independiente del formato regional de Windows
for /f %%i in ('venv\Scripts\python.exe -c "import datetime;print(datetime.datetime.now().strftime('%%Y-%%m-%%d_%%H%%M'))"') do set "STAMP=%%i"

echo Paso 1: Exportando datos desde Railway (Postgres)...
call venv\Scripts\python.exe manage.py dumpdata ^
    --natural-foreign --natural-primary ^
    --exclude contenttypes --exclude auth.Permission ^
    --exclude admin.logentry --exclude sessions.session ^
    --indent 2 ^
    -o "backups\altogas_%STAMP%.json"

if errorlevel 1 (
    echo.
    echo [ERROR] Fallo la exportacion. Revisa que BACKUP_DATABASE_URL sea correcta
    echo         y que el servicio Postgres en Railway este activo.
    pause
    exit /b 1
)

REM Paso 2 opcional: respaldo fisico completo si pg_dump esta instalado
where pg_dump >nul 2>&1
if %errorlevel%==0 (
    echo Paso 2: Generando dump completo con pg_dump...
    pg_dump "%DATABASE_URL%" -F c -f "backups\altogas_%STAMP%.dump"
) else (
    echo Paso 2: pg_dump no esta instalado - se omite el dump fisico completo.
    echo         El respaldo JSON ya contiene todos los leads y usuarios.
)

echo.
echo [OK] Respaldo generado en la carpeta: backups\
for %%F in (backups\altogas_%STAMP%.json) do echo   %%~nxF - %%~zF bytes
echo.
echo Recordatorio: los respaldos contienen datos personales de clientes.
echo No los subas a git (la carpeta backups\ ya esta ignorada).
pause
