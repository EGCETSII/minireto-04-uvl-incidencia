# Incidencia: no se encuentran modelos en un directorio externo

La validación funciona con el catálogo normal, pero falla cuando los modelos se encuentran en el directorio `external/models`.

## Entorno

Linux/macOS:

```bash
export CATALOG_FILE=external/catalog.csv
export UVL_MODELS_DIR=external/models
python validate.py
```

Windows PowerShell:

```powershell
$env:CATALOG_FILE="external/catalog.csv"
$env:UVL_MODELS_DIR="external/models"
python validate.py
```

## Resultado esperado

La validación debe terminar con `El catálogo es válido.`

## Resultado obtenido

La aplicación busca `weather.uvl` dentro de `models/` e informa de que el fichero no existe.
