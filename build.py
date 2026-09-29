import os
from pathlib import Path

from catalog import build_site

build_site(
    Path("site"),
    generate_diagrams=os.environ.get("GENERATE_DIAGRAMS") == "1",
)
print("Sitio generado en site/index.html")
