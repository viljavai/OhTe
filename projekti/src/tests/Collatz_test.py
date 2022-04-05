import unittest
from collatz import Conjecture

class TestConjecture(unittest.TestCase):
    def setUp(self):
        self.c = Conjecture(16)
    
    def test_oper_odd(self):
        c = Conjecture(11)
        c.oper()
        self.assertEqual((c.oper()), 17)

    def test_oper_even(self):
        self.c.oper()
        self.assertEqual((self.c.oper()), 4)
    
    def test_traverse(self):
        self.c.traverse()
        self.assertEqual(len(self.c.traverse()), 5)