# Minirreto 4: reproducir y depurar una incidencia

Este repositorio contiene una aplicación pequeña y un defecto intencionado. El objetivo no es encontrarlo por ensayo y error, sino seguir una metodología:

1. estudiar el informe;
2. reproducir el fallo en el entorno indicado;
3. registrar evidencias e hipótesis;
4. diagnosticar la causa;
5. escribir una prueba de regresión;
6. reparar y validar;
7. dejar trazabilidad en la incidencia y en el commit.

## Preparación

```bash
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
# .venv\Scripts\activate      # Windows PowerShell
python -m pip install -r requirements-dev.txt
python -m pytest
python build.py
```

El informe recibido está en `INCIDENCIA.md`. No inspecciones el código buscando directamente una línea sospechosa: reproduce primero el comportamiento descrito.
