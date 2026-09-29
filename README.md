# 🎓 Sistema Académico – Instituto Tecnológico Saint-Exupéry

Aplicación web desarrollada con **Django** para gestionar cursos, estudiantes, trabajos prácticos y entregas de una institución educativa. Trabajo práctico grupal del instituto San Jose.

---

##  Descripción

El sistema permite administrar desde un único lugar la información académica de la institución, con una interfaz moderna y responsive. Los usuarios pueden registrarse, iniciar sesión, tener un perfil con foto y trabajar con los distintos módulos del sistema.

##  Funcionalidades

- **Autenticación de usuarios:** registro, inicio de sesión y perfil con avatar.
- **Cursos:** alta, edición y baja, con imagen, fecha de inicio, fecha de fin y estado activo/inactivo.
- **Estudiantes:** listado, detalle, alta, edición y baja.
- **Trabajos prácticos y entregas:** carga de entregas con archivos adjuntos y calificación.
- **Interfaz responsive** con Bootstrap, animaciones y diseño institucional.

##  Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3.14 | Lenguaje principal |
| Django 6.0 | Framework web |
| SQLite | Base de datos (por defecto) |
| Pillow | Manejo de imágenes (`ImageField`) |
| Bootstrap 5.3 | Estilos y diseño responsive |
| Bootstrap Icons | Íconos |
| Animate.css | Animaciones |
| Google Fonts | Tipografías (Cormorant Garamond, Poppins) |

##  Requisitos previos

- [Python 3.12 o superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- Editor de código (recomendado: VS Code)

## 🚀 Instalación y puesta en marcha

**1. Clonar el repositorio**

```bash
git clone https://github.com/cotisanddoval/PythonProyecto1.git
cd PythonProyecto1
```

**2. Crear y activar el entorno virtual**

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

En Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Si PowerShell bloquea la ejecución de scripts, correr una sola vez:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**3. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

Si el archivo no existe, instalar manualmente:

```bash
pip install django pillow
```

**4. Aplicar las migraciones** (desde la carpeta que contiene `manage.py`)

```bash
cd Proyecto1
python manage.py migrate
```

**5. Crear un superusuario** (opcional, para acceder al panel de administración)

```bash
python manage.py createsuperuser
```

**6. Iniciar el servidor**

```bash
python manage.py runserver
```

Abrir en el navegador: **http://127.0.0.1:8000/**

El panel de administración está disponible en **http://127.0.0.1:8000/admin/**

##  Estructura del proyecto

```
PythonProyecto1/
├── Proyecto1/
│   ├── accounts/          # App de usuarios: registro, login y perfil
│   ├── myapp/             # App principal: cursos, estudiantes, entregas
│   │   ├── migrations/
│   │   ├── static/
│   │   │   ├── css/       # Estilos (style.css)
│   │   │   └── img/       # Logo e íconos
│   │   ├── templates/myapp/
│   │   ├── models.py
│   │   ├── views.py
│   │   └── urls.py
│   ├── templates/         # Plantilla base y templates de accounts
│   ├── media/             # Archivos subidos (imágenes de cursos, entregas)
│   ├── Proyecto1/         # Configuración del proyecto (settings, urls)
│   ├── db.sqlite3
│   └── manage.py
├── requirements.txt
└── README.md
```

## Flujo de trabajo en equipo (Git)

Antes de empezar a trabajar, traer los cambios del equipo:

```bash
git pull
```

Al terminar, subir los cambios propios:

```bash
git add .
git commit -m "descripción breve de lo realizado"
git push
```

Después de un `git pull` que traiga migraciones nuevas, correr `python manage.py migrate`.

##  Integrantes

- Lucero Lasala
- Leonel Sosa
- Constanza Sandoval


**Materia:** *Laboratorio de Programacion II*
**Año:** 2026



 Proyecto con fines educativos.
