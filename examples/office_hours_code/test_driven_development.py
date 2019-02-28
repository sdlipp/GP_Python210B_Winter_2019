import unittest
from order_food import *

class RestaurantTest(unittest.TestCase):

    def test_enter_order(self):
        self.assertEqual(enter_order('A hamburger, please'), 'hamburger')
        #self.assertEqual(enter_order('I would like a pizza'), 'pizza')

    def test_greet_customer(self):
        self.assertEqual(greet_customer('Florence'), 'Hello, Florence')