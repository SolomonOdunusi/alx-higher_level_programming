#!/usr/bin/python3
"""Defines unit tests for the Rectangle class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class"""

    def setUp(self):
        """Reset nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Test id"""
        r1 = Rectangle(10, 11)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(12, 13, 0, 0, 12)
        self.assertEqual(r2.id, 12)
        r3 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(r3.id, 7)

    def test_width(self):
        """Test width"""
        r1 = Rectangle(10, 11)
        self.assertEqual(r1.width, 10)
        r2 = Rectangle(12, 13, 0, 0, 12)
        self.assertEqual(r2.width, 12)
        r3 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(r3.width, 2)

    def test_height(self):
        """Test height"""
        r1 = Rectangle(10, 11)
        self.assertEqual(r1.height, 11)
        r2 = Rectangle(12, 13, 0, 0, 12)
        self.assertEqual(r2.height, 13)
        r3 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(r3.height, 4)

    def test_x(self):
        """Test x"""
        r1 = Rectangle(10, 11)
        self.assertEqual(r1.x, 0)
        r2 = Rectangle(12, 13, 0, 0, 12)
        self.assertEqual(r2.x, 0)
        r3 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(r3.x, 5)

    def test_y(self):
        """Test y"""
        r1 = Rectangle(10, 11)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(12, 13, 0, 0, 12)
        self.assertEqual(r2.y, 0)
        r3 = Rectangle(2, 4, 5, 6, 7)
        self.assertEqual(r3.y, 6)

    def test_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 1)

    def test_height_typeerror(self):
        """Test height TypeError"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, "3")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, {"1": 2})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, (1, ))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, None)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, float('nan'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, float('inf'))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(2, float('-inf'))

    def test_x_typeerror(self):
        """Test x TypeError"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, "4")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, {"1": 2})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, (1, ))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, float('nan'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, float('inf'))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(2, 3, float('-inf'))

    def test_y_typeerror(self):
        """Test y TypeError"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, "5")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, {"1": 2})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, (1, ))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, float('nan'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, float('inf'))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(2, 3, 4, float('-inf'))

    def test_width_valueerror(self):
        """Test width ValueError"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 2)

    def test_height_valueerror(self):
        """Test height ValueError"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)

    def test_x_valueerror(self):
        """Test x ValueError"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -234)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3, 4)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -234, 4)

    def test_y_valueerror(self):
        """Test y ValueError"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -234)

    def test_area(self):
        """Test area"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_str(self):
        """Test __str__"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
        r3 = Rectangle(5, 5)
        self.assertEqual(str(r3), "[Rectangle] (2) 0/0 - 5/5")

    def test_update_args(self):
        """Test update *args"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Test update **kwargs"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dictionary(self):
        """Test to_dictionary"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1,
                                         'height': 2,
                                         'width': 10})
        self.assertEqual(type(r1_dictionary), dict)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertNotEqual(r1, r2)

    def test_to_json_string(self):
        """Test to_json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(dictionary), dict)
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_empty(self):
        """Test to_json_string empty"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        self.assertEqual(type(json_dictionary), str)


if __name__ == "__main__":
    unittest.main()
