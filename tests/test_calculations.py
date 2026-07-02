from geo_calculator.calculations import find_average, gardners_equation
import pytest

def test_find_average_given_list_of_numbers():
    numbers = [1, 2, 3, 4, 5, 6]

    result = find_average(numbers)

    assert result == 3.5

def test_gardners_equation() -> None:
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)