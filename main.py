import tkinter as tk
from tkinter import ttk
from components.Todo import TodoFrame




class MainApplication ():

    def __init__ (self, master):

        # Set up the master widgets
        self.master = master
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill='both', expand=True)


        # Creating the todo frame
        self.TodoFrame = TodoFrame(self.notebook)
        self.TodoFrame2 = TodoFrame(self.notebook)
        self.notebook.add(self.TodoFrame.widget, text = "Todo")









root = tk.Tk()

root.title("Todo App")
root.minsize(640, 320)

main = MainApplication(root)
root.mainloop()