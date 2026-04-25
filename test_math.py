import unittest
<<<<<<< HEAD

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
=======
from my_math import abs_val, area_of_circle, circumference_of_circle

class TestMyMath(unittest.TestCase):

    # ----- abs_val tests -----
    def test_abs_val_basic(self):
        self.assertEqual(abs_val(5), 5)
        self.assertEqual(abs_val(-3), 3)
        self.assertEqual(abs_val(0), 0)

    def test_abs_val_invalid(self):
        with self.assertRaises(TypeError):
            abs_val("hello")


    # ----- area_of_circle tests -----
    def test_area_basic(self):
        self.assertAlmostEqual(area_of_circle(2), 12.5664)
        self.assertAlmostEqual(area_of_circle(0), 0)

    def test_area_invalid(self):
        with self.assertRaises(TypeError):
            area_of_circle("hi")
        with self.assertRaises(ValueError):
            area_of_circle(-1)

    def test_abs_val_float(self):
        self.assertEqual(abs_val(-3.5), 3.5)

    def test_abs_val_large(self):
        self.assertEqual(abs_val(-1000000), 1000000)

    def test_area_float(self):
        self.assertAlmostEqual(area_of_circle(2.5), 19.635)

    def test_area_small(self):
        self.assertAlmostEqual(area_of_circle(0.5), 0.7854)

    def test_circumference_basic(self):
        self.assertAlmostEqual(circumference_of_circle(2), 12.5664)

    def test_circumference_zero(self):
        self.assertEqual(circumference_of_circle(0), 0)

    def test_circumference_invalid(self):
        with self.assertRaises(ValueError):
            circumference_of_circle(-1)


if __name__ == "__main__":
    unittest.main()
>>>>>>> 7d57d4f4eaf95b832916baa2267fb2504c44d760
