# EntregaFinal-Roldan

Plataforma web para la gestión de contenido con blog, páginas estáticas, sistema de usuarios y perfiles.

## Descripción del Proyecto

Este proyecto es una aplicación web desarrollada con Django que ofrece un sistema completo para la gestión de contenido. Permite la creación y visualización de publicaciones de blog dinámicas, así como la administración de páginas estáticas. Además, incorpora un sistema de autenticación de usuarios con perfiles personalizables y la funcionalidad de comentarios en las publicaciones del blog.

## Cómo Funciona

La plataforma ofrece las siguientes funcionalidades principales:

* **Navegación Pública:** Los usuarios pueden explorar las publicaciones del blog en la página de inicio y acceder a las páginas estáticas a través de un listado.
* **Visualización de Contenido:** Cada publicación del blog tiene su propia página de detalle, y las páginas estáticas muestran información específica.
* **Autenticación de Usuarios:** Los usuarios pueden registrarse, iniciar sesión y cerrar sesión para acceder a funcionalidades adicionales.
* **Gestión de Usuarios (Perfil):** Los usuarios registrados pueden ver y editar su perfil, incluyendo información personal y la posibilidad de cambiar su contraseña.
* **Comentarios:** Los usuarios autenticados pueden dejar comentarios en las publicaciones del blog, fomentando la interacción.
* **Administración de Contenido:** Los administradores (a través del panel de administración de Django) tienen control total sobre la creación, edición y eliminación de páginas estáticas. Usuarios autorizados también pueden gestionar las publicaciones del blog desde el frontend.

### Requisitos Previos

* Python 3.x
* Django [indicar la versión de Django utilizada]
* Otras dependencias (listadas en `requirements.txt` si existe)

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/sindresorhus/del](https://github.com/sindresorhus/del)
    cd EntregaFinal-Roldan
    ```
2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # En Linux/macOS
    venv\Scripts\activate.bat  # En Windows
    ```
3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Aplica las migraciones:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Crea un superusuario (para la administración):**
    ```bash
    python manage.py createsuperuser
    ```

### Ejecución

```bash
python manage.py runserver
