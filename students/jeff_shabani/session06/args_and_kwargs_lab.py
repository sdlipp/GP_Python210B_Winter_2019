import unittest

def colors(fore_color='white', back_color = 'black', link_color = 'green', visited_color = 'blue'):
    result = (fore_color, back_color, link_color, visited_color)
    print(fore_color)

colors('red')
print(colors('red') == colors())

class MyTests(unittest.TestCase):

    # def test_short_anagram(self):
    #     self.assertTrue(is_anagram("tea", "eat"))

    def test_colors(self):
        test_vals = ('red', 'blue', 'yellow', 'chartreuse')
        expected = (test_vals[0], test_vals[1], test_vals[2], test_vals[3])
        actual = colors(*test_vals)
        self.assertEqual(colors(test_vals, expected))

if __name__ == '__main__':
    unittest.main()