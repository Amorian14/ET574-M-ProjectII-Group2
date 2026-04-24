import unittest
from my_math import abs_val, lcm, area_of_circle


class TestAbsVal(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(abs_val(5), 5)

    def test_negative(self):
        self.assertEqual(abs_val(-3.5), 3.5)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            abs_val("hello")


class TestLCM(unittest.TestCase):
    def test_two_numbers(self):
        self.assertEqual(lcm(4, 6), 12)

    def test_multiple_numbers(self):
        self.assertEqual(lcm(3, 4, 5), 60)

    def test_zero_case(self):
        self.assertEqual(lcm(0, 10), 0)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            lcm(3, "x")

    def test_not_enough_args(self):
        with self.assertRaises(ValueError):
            lcm(5)


class TestAreaOfCircle(unittest.TestCase):
    def test_typical(self):
        self.assertAlmostEqual(area_of_circle(2), 12.566370614359172)

    def test_zero_radius(self):
        self.assertEqual(area_of_circle(0), 0)

    def test_negative_radius(self):
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            area_of_circle("r")


if __name__ == "__main__":
    unittest.main()
