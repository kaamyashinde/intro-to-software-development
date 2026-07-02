def find_average(numbers):
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    return sum(numbers) / len(numbers)

def gardners_equation(velocity):
    """Calculate the density of a material using the Gardners equation
    Args:
        velocity: The velocity of the material
    Returns:
        The density of the material
    """
    if velocity <= 0:
        raise ValueError("Velocity must be greater than 0")
    return 0.31 * velocity ** 0.25

def inverse_gardners_equation(density):
    """Calculate velocity from density using the inverse Gardner's equation
    Args:
        density: The density of the material in g/cm3
    Returns:
        The velocity of the material in m/s
    """
    if density <= 0:
        raise ValueError("Density must be greater than 0")
    return (density / 0.31) ** 4