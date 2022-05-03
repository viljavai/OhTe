import unittest
import tkinter as tk
from collatz import Conjecture

class TestConjecture(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.c = Conjecture(10,self.master)
        self.odd = Conjecture(3,self.master)
        self.even = Conjecture(4,self.master)
    
    def test_oper_odd(self):
        self.assertEqual(int(self.odd.oper(3)), 10)

    def test_oper_even(self):
        self.assertEqual(int(self.even.oper(4)), 2)
    
    def test_traverse(self):
        self.assertEqual(len(list(self.c.traverse(10))), 7)
