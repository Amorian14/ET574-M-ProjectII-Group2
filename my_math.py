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
