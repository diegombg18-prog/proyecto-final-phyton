# Blog Web - Proyecto Final Python Coderhouse

Proyecto final desarrollado para el curso de Python en Coderhouse. Consiste en una aplicación web tipo Blog construida con **Django**, que incluye gestión completa de contenidos (CRUD), sistema de autenticación de usuarios, perfiles personalizados con avatares, sistema de búsqueda y rutas protegidas.

---

## 🚀 Funcionalidades Principales

- **Gestión de Publicaciones (CRUD Completo):** 
  - Creación, lectura, edición y eliminación de posts desde la interfaz web.
  - Soporte para carga de imágenes en cada publicación con manejo de respuestas robustas.
- **Sistema de Usuarios y Perfiles:** 
  - Registro de nuevos usuarios, inicio de sesión (Login) y cierre de sesión (Logout).
  - Creación automática de un modelo `Perfil` vinculado mediante una relación `OneToOneField` y señales (`signals`).
  - Edición de datos de usuario y carga de imagen de perfil (avatar) / biografía.
- **Buscador Dinámico:** 
  - Filtrado de publicaciones por palabra clave en el título o contenido utilizando consultas avanzadas de Django (`Q objects`).
- **Seguridad y Rutas Protegidas:** 
  - Control de acceso mediante `LoginRequiredMixin` y decoradores para asegurar que sólo los usuarios autenticados puedan crear, editar o eliminar posts y gestionar su perfil.

---

## 🛠️ Tecnologías y Dependencias

- **Lenguaje:** Python 3.x
- **Framework Web:** Django 5.x[cite: 14]
- **Base de Datos:** SQLite[cite: 14] (Desarrollo local)
- **Gestión de Imágenes:** Pillow[cite: 14]
- **Frontend:** HTML5, CSS3, Bootstrap[cite: 14]

---

## 📁 Estructura del Proyecto

```text
codigo_blog_web_final/
│
├── blog_config/          # Configuración principal del proyecto (settings, urls, wsgi)
├── posts/                # Aplicación de publicaciones (CRUD, modelos, vistas, formularios)
├── usuarios/             # Aplicación de usuarios (perfiles, registro, login, señales)
├── static/               # Archivos estáticos (hojas de estilo CSS, imágenes base)
├── templates/            # Plantillas HTML globales y específicas de cada app
├── media/                # Carpeta para almacenamiento local de archivos subidos (avatares, posts)
├── .env.example          # Plantilla de variables de entorno
├── .gitignore            # Archivos ignorados por Git
├── manage.py             # Script de gestión de Django
└── requirements.txt      # Dependencias del proyecto

⚙️ Instrucciones de Instalación y Ejecución Local
Sigue estos pasos para clonar y poner en marcha el proyecto en tu entorno local:

Clonar el repositorio:

Bash
git clone https://github.com/nataliafrancia4211-droid/codigo_blog_web_final.git
cd codigo_blog_web_final
Crear y activar el entorno virtual:

Bash
python -m venv venv
# En Windows (Git Bash / PowerShell):
source venv/Scripts/activate
Instalar las dependencias:

Bash
pip install -r requirements.txt
Aplicar las migraciones a la base de datos:

Bash
python manage.py makemigrations
python manage.py migrate
Crear un superusuario (opcional para el panel admin):

Bash
python manage.py createsuperuser
Iniciar el servidor de desarrollo:

Bash
python manage.py runserver
Abre tu navegador e ingresa a: http://127.0.0.1:8000/

👤 Autor
DIEGO BARRETO GOMEZ

Curso de Python - Coderhouse