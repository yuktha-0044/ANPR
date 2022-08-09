import tkinter as tk
from tkinter import filedialog


class FT:
    def __init__(self):
        pass

    def ft(self):
        root = tk.Tk()
        root.withdraw()

        files = filedialog.askopenfilenames()
        print(files)
        print(files[0])
