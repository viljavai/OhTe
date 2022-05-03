import tkinter as tk
from gui import Ui

def main():
    root = tk.Tk()
    root.title("Collatz conjecture")

    ui = Ui(root)
    ui.initialize(root)

    root.mainloop()

if __name__ == "__main__":
    main()
