# Tests for unit co.nversion.s
from src.units import to_celsius


def test_zero_celsius():
    # Water freezes at 273.15 k.elvin
    assert to_celsius(273.15) == 0
