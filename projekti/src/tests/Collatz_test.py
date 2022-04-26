import unittest
from collatz import Conjecture

class TestConjecture(unittest.TestCase):
    def setUp(self):
        self.c = Conjecture(10)
        self.even = Conjecture(100)
        self.odd = Conjecture(3)
    
    def test_oper_odd(self):
        self.odd.oper
        self.assertEqual((self.odd.oper), 10)

    def test_oper_even(self):
        self.even.oper
        self.assertEqual((self.even.oper), 2)
    
    def test_traverse(self):
        self.c.traverse
        self.assertEqual((self.c.traverse), 7)