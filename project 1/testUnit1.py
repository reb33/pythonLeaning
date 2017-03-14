import unittest
import functions1


class TestFactorial(unittest.TestCase):
    def test_1(self):
        self.assertEqual(functions1.factorial(5),120)

    def test_2(self):
        with self.assertRaises(TypeError):
            functions1.factorial(2.5)

if __name__ == '__main__':
    unittest.main()