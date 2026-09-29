import pytest

from catalog import classify_model_size


@pytest.mark.parametrize(
    ("feature_count", "expected"),
    [(1, "tiny"), (5, "tiny"), (6, "small"), (15, "small"),
     (16, "medium"), (30, "medium"), (31, "large")],
)
def test_classify_model_size(feature_count, expected):
    assert classify_model_size(feature_count) == expected
