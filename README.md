# 🎮 Steam Python

Plataforma web de reseñas de videojuegos inspirada en Steam, desarrollada con Django 5 y Tailwind CSS.

![Python](https://img.shields.io/badge/Python-3.13.7-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0.14-092E20?style=flat-square&logo=django&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-CDN-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-3.27.0-003B57?style=flat-square&logo=sqlite&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-PyMySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

---

## Descripción

Los usuarios pueden registrarse, publicar videojuegos con una imagen y escribir reseñas con puntuación decimal (0.0 – 5.0). La interfaz de tema oscuro usa Tailwind CSS sobre un sistema de colores personalizado cian/azul.

Soporta tres backends de base de datos: **SQLite** y **MySQL**.

> Prueba de Evaluación Parcial 2 — Programación en Python · Curso 2025-2026

---

## Stack Tecnológico

| | Tecnología | Versión |
|---|---|---|
| Backend | Django + Python | 5.0.14 / 3.13.7 |
| Frontend | Tailwind CSS (CDN) | 3.4.17 |
| Base de datos | SQLite / MySQL (PyMySQL) | 3.27.0 / 1.1.2 |
| Imágenes | Pillow + django-cleanup | 12.1.1 / 9.0.0 |

---

## Estructura

```
steam_python/
├── accounts/          # App autenticación (signup, login, logout)
├── reseñas/           # App principal
│   ├── models.py      # Modelos Juego y Resena
│   ├── views.py       # CBVs con LoginRequired y UserPassesTest
│   ├── urls.py        # Rutas de juegos y reseñas
│   └── forms.py       # ResenaForm
├── templates/         # base.html + todas las vistas
├── static/css/        # base.css (reset global)
├── media/posts/       # Imagenes subidas (nombre UUID)
├── steam_python/      # settings.py, urls.py raíz
├── db.sqlite3
└── manage.py
```

---

## Instalación

```bash
# 1. Clonar
git clone https://github.com/Carlos17082005/2526-PEP_PruebaEvaluacion2.git
cd 2526-PEP_PruebaEvaluacion2

# 2. Entorno virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 3. Dependencias
pip install -r requirements.txt

# 4. Base de datos
cd steam_python
python manage.py migrate

# 5. (Opcional) Datos de prueba
python seed.py

# 6. Superusuario
python manage.py createsuperuser

# 7. Servidor
python manage.py runserver
```

Abrir:
 - **https://carlos17082005.pythonanywhere.com**
 - **http://34.202.222.135**

---

## Permisos por rol

| Acción | Anónimo | Auth | Autor | Staff |
|---|:---:|:---:|:---:|:---:|
| Ver catálogo y detalle | ✅ | ✅ | ✅ | ✅ |
| Añadir juego | ❌ | ✅ | ✅ | ✅ |
| Editar / eliminar juego | ❌ | ❌ | ✅ | ✅ |
| Escribir reseña | ❌ | ✅ | ✅ | ✅ |
| Editar / eliminar reseña propia | ❌ | ✅ | ✅ | ✅ |
| Eliminar reseñas de otros | ❌ | ❌ | ❌ | ✅ |
| Panel `/admin/` | ❌ | ❌ | ❌ | ✅ |

---

## Documentación

**https://docs.google.com/document/d/1S700Qtk1pNbFWJ2S57n9bZFwfM75dwa07yUnv0jm3O0/edit?usp=sharing**

---

## Autores

**Carlos17082005** · **Alvaro-8D**