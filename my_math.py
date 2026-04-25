def pow_xy(x, y):
    """
    Name: pow_xy
    Purpose: Compute x raised to the power y without using Python's built-in pow().
    Parameters:
        x (int or float): Base value.
        y (int): Exponent (must be an integer).
    Returns:
        int or float: x raised to the power y.
    Raises:
        TypeError: If x is not a number or y is not an integer.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(y, int):
        raise TypeError("Exponent must be an integer")

    if y == 0:
        return 1
    if y < 0:
        return 1 / pow_xy(x, -y)

    result = 1
    for _ in range(y):
        result *= x

    return result

def distance(x1, y1, x2, y2):
    """
    Name: distance
    Purpose: Compute the distance between two points (x1, y1) and (x2, y2)
             without using the math module.
    Parameters:
        x1 (int or float): x-coordinate of the first point.
        y1 (int or float): y-coordinate of the first point.
        x2 (int or float): x-coordinate of the second point.
        y2 (int or float): y-coordinate of the second point.
    Returns:
        float: The distance between the two points.
    Raises:
        TypeError: If any parameter is not a number.
    """
    for v in (x1, y1, x2, y2):
        if not isinstance(v, (int, float)):
            raise TypeError("All coordinates must be numbers")

    dx = x2 - x1
    dy = y2 - y1
    squared = dx * dx + dy * dy

    if squared == 0:
        return 0.0

    guess = squared
    for _ in range(20):
        guess = 0.5 * (guess + squared / guess)

    return guess

