import unittest
from CheckClass import CheckClass


class Test1(unittest.TestCase):
    def setUp(self):
        self.v1 = CheckClass()

    def tearDown(self):
        pass

    def test_checkValue(self):
        # Test for positive case.
        val = self.v1.checkValue(3.2)
        self.assertEqual(val, 1)

        # Test for zero case.
        val = self.v1.checkValue(0)
        self.assertEqual(val, 0)

        # Test for negative case.
        # val = self.v1.checkValue(-5)
        # self.assertEqual(val, -1)

        # Test for TypeError
        with self.assertRaises(TypeError):
            self.v1.checkValue(True)


if __name__ == "__main__":
    unittest.main()
