import pytest
from planetweight import weight_on_planet

def test_weight_on_mars():
    assert weight_on_planet(100, 'Mars') == pytest.approx(371.0)

def test_weight_on_earth():
    assert weight_on_planet(50, 'Earth') == pytest.approx(490.5)

def test_default_planet():
    assert weight_on_planet(10) == pytest.approx(37.1)

def test_invalid_planet():
    with pytest.raises(ValueError):
        weight_on_planet(70, 'Gallifrey')
