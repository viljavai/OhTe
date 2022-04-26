import unittest
import tkinter as tk
from datetime import datetime
import os
from visualisazion import Plotting

class TestPlotting(unittest.TestCase):
    def __init__(self):
        master = tk.Tk()
        self.plot = Plotting(self,master,"color","background")
    
    def test_save_image(self):
        date = (datetime.now()).strftime("%m.%d.%Y-%H:%M:%S")
        filename = os.environ["HOME"] + "/my_collatz-" + date
        self.plot.save_image()
        self.assertEqual((self.plot.save_image), filename)