from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from time import strftime

class FrameTotalen(CTkFrame):
    def __init__(self, parent):
        CTkFrame.__init__(self,parent, bd=5, corner_radius=10)
        self.pack_propagate('false')

        CTkLabel(self, text="TOTALEN").grid(row=0, column=0)