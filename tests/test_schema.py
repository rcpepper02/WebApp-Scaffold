import pytest
from pydantic import ValidationError
from app.schemas.example import ExampleCreate

def test_example_create_accepts_name() -> None:
    assert ExampleCreate(name="test").name == "test"

def test_example_create_rejects_empty_name() -> None:
    with pytest.raises(ValidationError):
        ExampleCreate(name="")
