# Blog Web - Proyecto Final Python Coderhouse

Bienvenido al repositorio del proyecto final del curso de Python de Coderhouse. Se trata de un Blog Web desarrollado con Django que permite a los usuarios leer publicaciones, registrarse, iniciar sesión y gestionar sus propios posts con imágenes.

## 🚀 Funcionalidades Principales

- **Gestión de Publicaciones (CRUD):** Creación, lectura, edición y eliminación de posts desde la interfaz web.
- **Soporte de Imágenes:** Carga y visualización de imágenes asociadas a cada publicación (con manejo responsivo si no hay imagen).
- **Sistema de Búsqueda:** Buscador por palabra clave en título o contenido de las publicaciones.
- **Autenticación de Usuarios:** Registro de nuevos usuarios, inicio de sesión (login) y cierre de sesión (logout).
- **Rutas Protegidas:** Protección en el backend mediante `LoginRequiredMixin` y decoradores para asegurar que solo usuarios autenticados puedan crear, editar o eliminar contenidos.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework Web:** Django 5.x
- **Base de Datos:** SQLite
- **Manejo de Imágenes:** Pillow
- **Frontend:** HTML5, CSS3, Bootstrap

## ⚙️ Instrucciones de Instalación y Ejecución

Sigue estos pasos para clonar y ejecutar el proyecto localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone <URL_DE_TU_REPOSITO_GITHUB>
   cd codigo_blog_web_final