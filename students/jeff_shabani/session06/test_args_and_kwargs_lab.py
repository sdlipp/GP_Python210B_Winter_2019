import unittest

from students.jeff_shabani.session06.args_and_kwargs_lab import colors

class MyTests(unittest.TestCase):


    def test_args(self):
        test_vals = ('red', 'blue', 'yellow', 'chartreuse')
        expected = (test_vals[0], test_vals[1], test_vals[2], test_vals[3])
        actual = colors(*test_vals)
        self.assertEqual (expected, actual)

    def test_kwargs(self):
        test_vals = {'link_color':'red', 'back_color':'blue'}
        expected = ('white', 'blue', 'red', 'blue')
        actual = colors(**test_vals)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()