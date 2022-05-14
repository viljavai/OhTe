import tkinter as tk
from logic.collatz import Conjecture
from visualisazion.visualisazion import Plotting

class Ui:
    def __init__(self, master):
        """UI:n alustus

        Args:
            master: tkinter-olio
        """
        self.master = master

        self.savebutton = None
        self.integer_input = None
        self.integer_entry = None
        self.angle_input = None
        self.angle_entry = None
        self.numvar_box = None
        self.checkbox = None
        self.integerbutton = None
        self.integer = None
        self.angle = None
        self.numvar = None
        self.canvas = None

    def initialize(self):
        """Alustetaan UI, napit ja syöttökentät

        """
        self.canvas = tk.Canvas(self.master)

        save_instance = Plotting(self.master, self.canvas)
        self.savebutton = tk.Button(self.master,
        text="Save graph", command=save_instance.save_image)

        self.savebutton.config(bg="black",fg="white")
        self.savebutton.pack()

        self.integer_input = tk.Label(self.master, text="Give integer")
        self.integer_input.pack()

        self.integer_entry = tk.Entry(self.master)
        self.integer_entry.pack()

        self.angle_input = tk.Label(self.master, text="Give angle of rotation")
        self.angle_input.pack()

        self.angle_entry = tk.Entry(self.master)
        self.angle_entry.pack()
        self.angle_entry.insert(0,"10")

        self.numvar_box = tk.BooleanVar(self.master)
        self.checkbox = tk.Checkbutton(self.master, text="Show numbers on graph",
        variable=self.numvar_box, onvalue=True, offvalue=False)

        self.checkbox.pack()

        self.integerbutton = tk.Button(text="Create graph", command=self.press)
        self.integerbutton.config(bg="black",fg="white")
        self.integerbutton.pack()

    def press(self):
        """Napin toiminta
        """
        self.integer = self.integer_entry.get()
        if self.integer == "1" or self.integer[0] == "-":
            return print("Syötäthän vain päteviä numeroita syöttökenttiin!")
        try:
            self.integer = int(self.integer)
        except:
            return print("Syötäthän vain päteviä numeroita syöttökenttiin!")
        self.angle = self.angle_entry.get()
        if self.angle[0] == "-":
            return print("Syötäthän vain päteviä numeroita syöttökenttiin!")
        try:
            self.angle = int(self.angle)
        except:
            return print("Syötäthän vain päteviä numeroita syöttökenttiin!")
        self.numvar = self.numvar_box.get()
        instance = Conjecture(self.integer, self.master, self.canvas, self.angle, self.numvar)
        instance.tree()
