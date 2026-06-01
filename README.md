# TP Git + GitHub y Python — Calidad de Software ---------

Aplicación mínima en Python desarrollada en equipo como trabajo práctico de la materia **Calidad de Software**. El objetivo del TP es practicar un flujo colaborativo completo con Git y GitHub, e implementar un pipeline de CI con GitHub Actions.

La app muestra por consola una tabla con nombre, edad y email de personas cargadas en el sistema.

---

## Requisitos

- Python 3.11 o superior

---

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/CalidadSoftware2026/TP-Git-Github-y-Python.git
cd TP-Git-Github-y-Python
```

Crear y activar un entorno virtual:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python -m venv .venv
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecutar la app

```bash
python src/app.py
```

La salida muestra una tabla con los datos de las personas registradas:

```
Personas
┌─────────┬───────┬────────────────────┐
│ Nombre  │ Edad  │ Email              │
├─────────┼───────┼────────────────────┤
│ Uriel   │ 25    │ uriel@email.com    │
│ Valen   │ 24    │ valen@email.com    │
└─────────┴───────┴────────────────────┘
```

---

## Ejecutar los tests

```bash
pytest --cov=. --cov-report=term-missing
```

Para ver el reporte de cobertura en formato XML (usado en CI):

```bash
pytest --cov=. --cov-report=term-missing --cov-report=xml
```

---

## Verificaciones de formato y linting

Este proyecto usa [ruff](https://docs.astral.sh/ruff/) como formatter y linter.

Verificar formato:

```bash
ruff format --check .
```

Aplicar formato automáticamente:

```bash
ruff format .
```

Ejecutar el linter:

```bash
ruff check .
```

---

## CI con GitHub Actions

El repositorio cuenta con un workflow de CI en `.github/workflows/ci.yml` que se ejecuta automáticamente en cada push y pull request a `main`. El pipeline corre dos jobs en paralelo:

- **Lint y formato**: verifica que el código cumpla con las reglas de ruff.
- **Tests y cobertura**: ejecuta pytest y genera un reporte de cobertura.

Si alguno de los dos falla, el PR no puede mergearse.

---

## Flujo de trabajo con Git

1. Cada integrante crea su propia rama a partir de `main`:
   ```bash
   git checkout -b nombre_branch
   ```
2. Realiza sus cambios y los commitea con mensajes descriptivos:
   ```bash
   git add .
   git commit -m "descripción del cambio"
   ```
3. Antes de abrir un PR, trae los cambios de `main` a su rama:
   ```bash
   git fetch origin
   git merge origin/main
   ```
4. Sube la rama y abre un Pull Request hacia `main` en GitHub.
5. Otro integrante revisa el PR y lo aprueba.
6. Una vez aprobado y con el CI en verde, se mergea a `main`.

---

## Estructura del proyecto

```
TP-Git-Github-y-Python/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── app.py
│   └── person.py
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   └── test_person.py
├── .gitignore
├── requirements.txt
└── README.md
```