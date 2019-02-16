import unittest

def colors(fore_color='white', back_color = 'black', link_color = 'green', visited_color = 'blue'):
    print(fore_color, back_color, link_color, visited_color)

#colors()

test_vals = ('red', 'blue', 'yellow', 'chartreuse')
expected = test_vals[0], test_vals[1], test_vals[2], test_vals[3]

colors(*test_vals)
print(colors(*test_vals) == expected)
# print(test_vals == expected)

# class MyTests(unittest.TestCase):
#
#     def test_colors(self):
#         test_vals = ('red', 'blue', 'yellow', 'chartreuse')
#         expected = (test_vals[0], test_vals[1], test_vals[2], test_vals[3])
#         actual = colors(*test_vals)
#         self.assertEqual(expected, actual)
#
# if __name__ == '__main__':
#     unittest.main()