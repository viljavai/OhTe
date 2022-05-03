import tkinter as tk
from collatz import Conjecture
from visualisazion import Plotting

class Ui:
    def __init__(self, master):
        """UI:n alustus

        Args:
            master: tkinter-olio
        """
        self.master = master

    def initialize(self,master):
        """Alustetaan UI
        
        """
        save_instance = Plotting(self.master)
        self.savebutton = tk.Button(self.master, text="Save graph", command=save_instance.save_image)
        self.savebutton.config(bg="black",fg="white")
        self.savebutton.pack()

        self.integer_input = tk.Label(self.master, text="Anna luku n")
        self.integer_input.pack()
        #self.bgcolor_input = tk.Label(self.master, text="Taustaväri")
        #self.bgcolor_input.pack()

        self.integer_entry = tk.Entry(self.master)
        self.integer_entry.pack()
        #self.bgcolor_entry = tk.Entry(self.master)

        self.integerbutton = tk.Button(text="Create graph", command=self.press)
        self.integerbutton.config(bg="black",fg="white")
        self.integerbutton.pack()

    def press(self):
        """Napin toiminta
        """
        self.integer = self.integer_entry.get()
        self.integer = int(self.integer)
        instance = Conjecture(self.integer, self.master)
        instance.tree(self.integer, self.master)
        