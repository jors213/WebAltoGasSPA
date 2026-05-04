@echo off
echo ============================================
echo  Alto Gas SPA - Compilando Tailwind CSS v4
echo ============================================

echo Paso 1: Compilando y minificando CSS...
call venv\Scripts\tailwindcss.exe -i ./input.css -o ./core/static/core/css/tailwind.css --minify

echo Paso 2: Recolectando archivos estaticos...
call venv\Scripts\python.exe manage.py collectstatic --noinput

echo.
echo [OK] Todo listo. CSS en: core/static/core/css/tailwind.css
for %%F in (core\static\core\css\tailwind.css) do echo Tamano: %%~zF bytes
pause
