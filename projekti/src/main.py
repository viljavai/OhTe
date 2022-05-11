import tkinter as tk
from UI.gui import Ui

def main():
    root = tk.Tk()
    root.title("Collatz conjecture")

    user_interface = Ui(root)
    user_interface.initialize()

    root.mainloop()

if __name__ == "__main__":
    main()
