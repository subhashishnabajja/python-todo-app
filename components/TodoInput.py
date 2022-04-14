import tkinter as tk
from tkinter import ttk

class TodoInput (tk.Frame):

    def __init__(self, container, input = None, onSubmit=None ):
        super().__init__(container)
        self.onSubmit = onSubmit
        self.todos = []
        self.configure(height = 70)
        ttk.Style().configure('pad.TEntry', padding='5 5 5 5')
        self.inputText = input
        self.input = ttk.Entry(self, font = ("Arial 14"), style='pad.TEntry', textvariable=self.inputText)
        self.input.bind("<Return>", self.handleAddTodo)
        self.input.place(relx = .45, rely = .5, relwidth = .50, anchor = tk.CENTER)

        self.addBtn = tk.Button(self, text = "Add", command=self.handleAddTodo )
        self.addBtn.place(rely=.5, relx=.775, relheight=.5, relwidth=.12, anchor = tk.CENTER)

    def handleAddTodo(self, *args):
        text = self.inputText.get()
        if text != "":
            self.onSubmit(text)
            self.inputText.set("")
    
