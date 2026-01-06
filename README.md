# Plataforma Corporativa AltoGas SPA ⚡

> **Una solución de transformación digital para la industria de certificación de gas en Chile.**

[![Live Demo](https://img.shields.io/badge/VISITAR-SITIO_WEB_EN_VIVO-orange?style=for-the-badge&logo=firefox)](https://www.altogasspa.cl)

## 💼 El Negocio y el Desafío

**Alto Gas SPA** es una empresa de ingeniería especializada en la certificación de sellos verdes (SEC) y reparación de fugas de gas. El cliente operaba principalmente a través de referidos y teléfono, careciendo de una presencia digital centralizada que validara su autoridad técnica ante nuevos clientes.

**El objetivo:** Crear una plataforma web que sirviera como canal principal de captación de leads (clientes potenciales) y digitalizara el catálogo de servicios técnicos, transmitiendo confianza y cumplimiento normativo.

## 🚀 Impacto y Solución Entregada

Desarrollé y desplegué una aplicación web Fullstack a medida que resuelve tres problemas clave del negocio:

1.  **Automatización de Contacto:** Implementación de un sistema que captura las solicitudes de los clientes y notifica instantáneamente al equipo técnico vía correo electrónico (SMTP), reduciendo el tiempo de respuesta.
2.  **Identidad de Marca:** Diseño de interfaz moderno y responsivo que eleva la percepción profesional de la empresa frente a competidores en el mercado.
3.  **Infraestructura Robusta:** Despliegue en un entorno de producción seguro (HTTPS) y escalable, garantizando disponibilidad 24/7 para consultas de emergencia.

## 🛠️ Stack Tecnológico

Este proyecto fue construido utilizando una arquitectura moderna y escalable:

* **Backend:** Python 3 + Django (Manejo de lógica de negocio y seguridad).
* **Frontend:** Tailwind CSS + HTML5 (Diseño responsivo y optimizado para móviles).
* **Base de Datos:** PostgreSQL (Gestión de datos en producción).
* **Infraestructura (DevOps):**
    * **Railway:** Hosting de aplicación y base de datos.
    * **Cloudflare:** Gestión de DNS, CDN y seguridad SSL.
    * **WhiteNoise:** Gestión eficiente de archivos estáticos.
    * **Gmail SMTP:** Integración para servicio de mensajería transaccional.

---

### 📸 Galería

<img width="100%" alt="Vista Home Desktop" src="https://github.com/user-attachments/assets/78cd5673-648f-47bb-af2b-e231e7bd632d" />
<br><br>

<img width="100%" alt="Vista Servicios" src="https://github.com/user-attachments/assets/8feb7125-2891-410e-aa2d-9ecf34243eff" />
<br><br>

<img width="100%" alt="Vista Contacto" src="https://github.com/user-attachments/assets/c55a3f36-8a47-4b51-9593-69f7ab8966a9" />

---

## 🔧 Ejecución Local (Para Desarrolladores)

Este proyecto requiere variables de entorno para funcionar correctamente en local.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/WebAltoGasSPA.git](https://github.com/tu-usuario/WebAltoGasSPA.git)
    cd WebAltoGasSPA
    ```

2.  **Crear entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuración:**
    Crea un archivo `.env` en la raíz basado en `.env.example` y configura tus credenciales de base de datos y SMTP.

5.  **Ejecutar:**
    ```bash
    python manage.py runserver
    ```

---
### 📄 Licencia
Este proyecto es de uso comercial exclusivo para **Alto Gas SPA**. El código fuente se expone aquí únicamente con fines de portafolio académico y profesional.
Designed & Developed by Jorge Soto - 2026.
