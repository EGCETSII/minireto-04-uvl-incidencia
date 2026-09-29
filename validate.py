from catalog import validate_catalog

errors = validate_catalog()
if errors:
    print("El catálogo no es válido:")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("El catálogo es válido.")
