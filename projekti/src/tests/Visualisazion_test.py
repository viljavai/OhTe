import unittest
import tkinter as tk
from datetime import datetime
import os
from visualisazion import Plotting

class TestPlotting(unittest.TestCase):
    def setUp(self):
        master = tk.Tk()
        self.plot = Plotting(master)
    
    def test_save_image(self):
        date = (datetime.now()).strftime("%m.%d.%Y-%H:%M:%S")
        filename = os.environ["HOME"] + "/my_collatz-" + date
        self.assertEqual((self.plot.save_image()), filename)