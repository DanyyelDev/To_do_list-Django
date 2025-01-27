# To_do_list-Django
# Proyecto Django: API de Gestión de Tareas (To-Do List)

Este proyecto es una API para gestionar una lista de tareas (To-Do list) utilizando Django y Django Rest Framework (DRF). La API permite realizar las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las tareas, y tiene implementado un sistema de autenticación mediante JWT (JSON Web Tokens). Además, se implementa una arquitectura de microservicios y tareas asíncronas utilizando Celery.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener los siguientes programas instalados:

- Python 3.8 o superior
- Django 4.0 o superior
- Django Rest Framework
- PostgreSQL (si se está usando como base de datos, o puedes usar SQLite para pruebas locales)

## Instalación

1. **Clona el repositorio:** https://github.com/DanyyelDev/To_do_list-Django.git
2. **Instala las dependencias:**

    Instala las dependencias necesarias que están en el archivo requirements.txt:
        pip install -r requirements.txt

3. **Aplica las migraciones:**
    Ejecuta las migraciones para crear las tablas en la base de datos:
        python manage.py migrate

3. **Ejecución del Proyecto**
    Inicia el servidor de desarrollo:
    Para ejecutar el servidor de desarrollo de Django, usa el siguiente comando:
        python manage.py runserver
    El servidor debería estar ejecutándose en http://127.0.0.1:8000/.


## API
Accede a la API:

Puedes acceder a la API a través de Postman o cualquier otra herramienta para enviar solicitudes HTTP. La URL base de la API es http://127.0.0.1:8000/api/.

Ejemplo de endpoint para obtener un token JWT:

POST /api/token/
Datos de la solicitud:

{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
Recibirás un access token y un refresh token que puedes usar para autenticar futuras solicitudes.

**Autenticación**
La API utiliza JSON Web Tokens (JWT) para la autenticación. Para obtener un token de acceso, realiza una solicitud POST al endpoint /api/token/ con el nombre de usuario y la contraseña en formato JSON.

Ejemplo de solicitud para obtener un token:

{
  "username": "usuario_de_prueba",
  "password": "contraseña_secreta"
}
La respuesta incluirá un token de acceso (access) y un token de actualización (refresh):

{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4MDE4NDY5LCJpYXQiOjE3MzgwMTY2NjksImp0aSI6IjVmOWFlNjQyNDUyYjQzNGI5MTA2MGQ3MTQzOGMzMTEwIiwidXNlcl9pZCI6MX0.VctrrWKGyuVXsuGC0Xm3fDUkTAKFx5wWXi80hjwNb0I",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczODEwMzA2OSwiaWF0IjoxNzM4MDE2NjY5LCJqdGkiOiIxZjg3ZmU3ZmJlNDM0Y2I5OTljMTYxZTY5YTc5ZmRjMCIsInVzZXJfaWQiOjF9.5i211gG4wbfcZmgO4Um2BxSgYKxsu4Aa0y10OYP5Tk0"
}
Usa el token de acceso en las cabeceras de tus solicitudes para autenticarte.

**Ejecutar Pruebas**
Escribir las pruebas:

Las pruebas de las vistas están en el archivo tasks/test_views.py. Este archivo contiene pruebas unitarias e integradas para los endpoints de la API.

Ejecutar las pruebas:

Para ejecutar las pruebas, usa el siguiente comando:

python manage.py test