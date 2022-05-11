import unittest
import tkinter as tk
from collatz import Conjecture

class TestConjecture(unittest.TestCase):
    def setUp(self):
        self.master = tk.Tk()
        self.canvas = tk.Canvas
        self.c = Conjecture(10,self.master, self.canvas, 10, False)
        self.odd = Conjecture(3,self.master, self.canvas, 10, False)
        self.even = Conjecture(4,self.master, self.canvas, 10, False)
    
    def test_oper_odd(self):
        self.assertEqual(int(self.odd.oper()), 10)

    def test_oper_even(self):
        self.assertEqual(int(self.even.oper()), 2)
    
    def test_traverse(self):
        self.assertEqual(len(list(self.c.traverse())), 7)
