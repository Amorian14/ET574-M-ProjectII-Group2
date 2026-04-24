"""
my_math.py
Custom Math Function Library for ET-574 Project II.

This module contains all group-defined mathematical functions, including:
- Core functions assigned to each team member
- Original math functions created by each member

All functions are implemented without using Python's built-in math module.

Group: ET574-M-ProjectII-Group2
Members: Morian, Ajani | Scott Dickens, Kadeem | Tiburcio, David
"""


def abs_val(x):
    """
    Name: abs_val
    Purpose: Return the absolute value of x without using Python's built-in abs().
    Parameters:
        x (int or float): A numeric value.
    Returns:
        int or float: The absolute value of x.
    Raises:
        TypeError: If x is not a number.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("abs_val only accepts int or float")

    if x < 0:
        return -x
    return x


def gcd_two(a, b):
    """
    Name: gcd_two
    Purpose: Compute the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    Parameters:
        a (int): First integer.
        b (int): Second integer.
    Returns:
        int: The greatest common divisor of a and b.
    """
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(*args):
    """
    Name: lcm
    Purpose: Compute the least common multiple (LCM) of two or more integers.
    Parameters:
        *args (int): Two or more integers.
    Returns:
        int: The LCM of all provided integers.
    Raises:
        ValueError: If fewer than two integers are provided.
        TypeError: If any argument is not an integer.
    """
    if len(args) < 2:
        raise ValueError("lcm requires at least two integers")

    for n in args:
        if not isinstance(n, int):
            raise TypeError("All arguments to lcm must be integers")

    def lcm_two(a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // gcd_two(a, b)

    current = args[0]
    for n in args[1:]:
        current = lcm_two(current, n)

    return current


def area_of_circle(r):
    """
    Name: area_of_circle
    Purpose: Compute the area of a circle with radius r.
    Parameters:
        r (float or int): Radius of the circle. Must be non-negative.
    Returns:
        float: Area of the circle.
    Raises:
        ValueError: If r is negative.
        TypeError: If r is not a number.
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Radius must be a number")
    if r < 0:
        raise ValueError("Radius cannot be negative")

    pi = 3.141592653589793
    return pi * r * r
