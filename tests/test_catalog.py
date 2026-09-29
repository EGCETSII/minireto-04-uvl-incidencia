from pathlib import Path

from catalog import count_features, validate_catalog


def test_count_features(model_factory):
    model = model_factory(["A", "B", "C"])
    assert count_features(model) == 4  # Root + A + B + C


def test_valid_catalog_has_no_errors(tmp_path: Path):
    models = tmp_path / "models"
    models.mkdir()
    (models / "simple.uvl").write_text(
        "features\n    Root\n        optional\n            A\n",
        encoding="utf-8",
    )
    catalog = tmp_path / "catalog.csv"
    catalog.write_text(
        "id,title,author,description,file\n"
        "simple,Simple,Ana,Example,simple.uvl\n",
        encoding="utf-8",
    )

    assert validate_catalog(catalog, models) == []


def test_missing_author_is_reported(tmp_path: Path):
    models = tmp_path / "models"
    models.mkdir()
    (models / "simple.uvl").write_text(
        "features\n    Root\n",
        encoding="utf-8",
    )
    catalog = tmp_path / "catalog.csv"
    catalog.write_text(
        "id,title,author,description,file\n"
        "simple,Simple,,Example,simple.uvl\n",
        encoding="utf-8",
    )

    errors = validate_catalog(catalog, models)
    assert any("falta el campo author" in error for error in errors)
