
from tkinter import ttk
from tkinter import StringVar


class TodoFrame():

    def __init__(self, master):
        self.master = master
        self.widget = ttk.Frame(master)
        self.widget.pack(fill = "both", expand = True)

        # Layout and widgets

        # Creating the input
        self.textInput = StringVar()
        self.textWidget = ttk.Entry(self.widget, textvariable=self.textInput)
        self.textWidget.pack()

