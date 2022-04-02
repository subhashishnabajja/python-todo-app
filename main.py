import tkinter as tk
from tkinter import ttk
from components.Todo import TodoFrame
class MainApplication(tk.Tk):

    def __init__(self):
        super().__init__()

        # Creating the notebook frame
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill = "both", expand = True)
    
        # Todo Frame
        self.TodoFrame = TodoFrame(self.notebook)
        self.TodoFrame.pack(fill="both", expand=True)

       
        self.notebook.add(self.TodoFrame, text = "Todo")

    





if __name__ == "__main__":
    root = MainApplication()
    root.geometry("640x500")
    root.mainloop()