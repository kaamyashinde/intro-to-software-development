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
    return 0.31 * velocity ** 0.25