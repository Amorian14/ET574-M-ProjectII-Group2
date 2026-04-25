import unittest

from my_math import pow_xy, distance

class TestPowXY(unittest.TestCase):
    def test_positive_exponent(self):
        self.assertEqual(pow_xy(2, 3), 8)

    def test_zero_exponent(self):
        self.assertEqual(pow_xy(5, 0), 1)

    def test_negative_exponent(self):
        self.assertAlmostEqual(pow_xy(2, -2), 0.25)

    def test_invalid_base_type(self):
        with self.assertRaises(TypeError):
            pow_xy("2", 3)

    def test_invalid_exponent_type(self):
        with self.assertRaises(TypeError):
            pow_xy(2, 3.5)

class TestDistance(unittest.TestCase):
    def test_same_point(self):
        self.assertEqual(distance(0, 0, 0, 0), 0.0)

    def test_horizontal_distance(self):
        self.assertAlmostEqual(distance(0, 0, 3, 0), 3.0, places=5)

    def test_vertical_distance(self):
        self.assertAlmostEqual(distance(0, 0, 0, 4), 4.0, places=5)

    def test_diagonal_distance(self):
        self.assertAlmostEqual(distance(0, 0, 3, 4), 5.0, places=2)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            distance(0, 0, "3", 4)
