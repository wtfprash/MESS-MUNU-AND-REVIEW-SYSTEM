import tkinter as tk
from src.gui import VitMessApp

def main():
    root = tk.Tk()
    app = VitMessApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
