from pathlib import Path

import pytest


@pytest.fixture
def model_factory(tmp_path: Path):
    def create(feature_names: list[str]) -> Path:
        lines = ["features", "    Root", "        optional"]
        lines.extend(f"            {name}" for name in feature_names)
        path = tmp_path / "model.uvl"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return path

    return create
