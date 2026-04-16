# django-taller

Proyecto Django llamado `taller_formularios_nombre_estudiantes` con dos aplicaciones independientes:

- `asistencia`
- `solicitudes`

## Requisitos

- Python 3.13
- Django 6.0.4

## Instalación de Django en este entorno

```powershell
& 'C:\Program Files\PostgreSQL\17\pgAdmin 4\python\python.exe' -m pip install --user Django
```

## Ejecutar el proyecto

```powershell
& 'C:\Program Files\PostgreSQL\17\pgAdmin 4\python\python.exe' manage.py migrate
& 'C:\Program Files\PostgreSQL\17\pgAdmin 4\python\python.exe' manage.py runserver
```

## Rutas principales

- `/`
- `/asistencia/`
- `/solicitudes/`
- `/admin/`

## Verificación rápida

```powershell
& 'C:\Program Files\PostgreSQL\17\pgAdmin 4\python\python.exe' manage.py check
& 'C:\Program Files\PostgreSQL\17\pgAdmin 4\python\python.exe' manage.py test
```

## Flujo Git

- `main` inicia sin código, solo con el README base.
- `dev` nace desde `main`.
- El desarrollo entra por ramas `feat/*`.
- Cada funcionalidad se integra a `dev` mediante merge dedicado.
