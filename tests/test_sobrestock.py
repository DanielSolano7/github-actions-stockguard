import pytest
from src.inventario import detectar_sobrestock


def test_hay_sobrestock():
    assert detectar_sobrestock(120, 100) is True


def test_limite_exacto_no_es_sobrestock():
    assert detectar_sobrestock(100, 100) is False


def test_sin_sobrestock():
    assert detectar_sobrestock(40, 100) is False


def test_maximo_invalido():
    with pytest.raises(ValueError):
        detectar_sobrestock(10, 0)