<<<<<<< HEAD
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

=======
def abs_val(x):
    """
    Name: abs_val
    Purpose: Returns the absolute value of a number
    Parameters: x (int or float)
    Returns: positive value of x
    """

    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError("abs_val(x) requires a number")

    if x < 0:
        return -x
    return x


def area_of_circle(r):
    """
    Name: area_of_circle
    Purpose: Calculates the area of a circle
    Parameters: r (radius)
    Returns: area of the circle
    """

    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("area_of_circle(r) requires a number")

    if r < 0:
        raise ValueError("radius cannot be negative")

    return 3.1416 * r * r

def circumference_of_circle(r):
    """
    Name: circumference_of_circle
    Purpose: Calculates the circumference of a circle
    Parameters: r (radius)
    Returns: circumference of the circle
    """

    if isinstance(r, bool) or not isinstance(r, (int, float)):
        raise TypeError("circumference_of_circle(r) requires a number")

    if r < 0:
        raise ValueError("radius cannot be negative")

    return 2 * 3.1416 * r
>>>>>>> 7d57d4f4eaf95b832916baa2267fb2504c44d760
