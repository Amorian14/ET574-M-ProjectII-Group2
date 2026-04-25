import unittest
from my_math import abs_val, area_of_circle

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


if __name__ == "__main__":
    unittest.main()
