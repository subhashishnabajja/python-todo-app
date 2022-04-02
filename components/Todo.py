import tkinter as tk
import datetime 
from tkinter import ttk
from database import db

TODO = db.TODO()
class TodoFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)
        self.state = {"todos":[], "date": tk.StringVar(value=datetime.datetime.now)}
        self.todos = tk.StringVar(value=self.state["todos"])

        self.DatePicker = DatePicker(self,  onChange=self.handleDateChange)
        self.DatePicker.pack(fill="both")

        self.TodoInput = TodoInput(self, onSubmit=self.handleTodoText)
        self.TodoInput.pack(fill = "both")

        self.TodoList = TodoList(self, list=self.todos, onDone=self.handleDone)
        self.TodoList.pack(fill = "both", expand=True)

    def handleTodoText (self, text):
        self.state["todos"].append(text)
        self.todos.set(self.state["todos"])
        print(self.state)
        TODO.addTodo(len(self.state["todos"]), text, self.state["date"])

    def handleDateChange(self, currDate):
        self.state["date"] = currDate
        print(self.state)
    

    def handleDone(self, currTodo):
        todos = self.state["todos"]
        todos.remove(currTodo)
        self.todos.set(todos)







class DatePicker (tk.Frame):

    def __init__(self, container, onChange = None):
        super().__init__(container)
        # States
        self.onChange = onChange


        self.configure(bg="red", height=50)

        """"
        Entry Widget Config
        """
        self.date = tk.StringVar(value = str(datetime.datetime.now().strftime("%d/%m/%y")))
        self.onChange(self.date.get())
        self.entry = tk.Entry(self, textvariable = self.date, justify="center")
        self.entry.place(rely = .5, relx=.5, relwidth = .55 ,relheight= .5, anchor= tk.CENTER)

        """"
        Increment Widget Config
        """
        self.DecrementBtn = tk.Button(self, text = "<", command = self.handleDecrement)
        self.DecrementBtn.place(rely = .5, relx=.20,relheight= .5, anchor= tk.CENTER)

        self.IncrementBtn = tk.Button(self, text = ">", command = self.handleIncrement)
        self.IncrementBtn.place(rely = .5, relx=.8 ,relheight= .5, anchor= tk.CENTER)

    def handleIncrement(self):
        currState = datetime.datetime.strptime(self.date.get(), "%d/%m/%y")
        incrementedState = currState + datetime.timedelta(days = 1)
        self.date.set(str(incrementedState.strftime("%d/%m/%y")))
        self.onChange(self.date.get())

    def handleDecrement(self):
        currState = datetime.datetime.strptime(self.date.get(), "%d/%m/%y")
        incrementedState = currState - datetime.timedelta(days = 1)
        self.date.set(str(incrementedState.strftime("%d/%m/%y")))
        self.onChange(self.date.get())





class TodoInput (tk.Frame):

    def __init__(self, container, onSubmit=None ):
        super().__init__(container)
        self.onSubmit = onSubmit
        self.todos = []
        self.configure(bg="pink", height = 70)
        ttk.Style().configure('pad.TEntry', padding='5 5 5 5')
        self.inputText = tk.StringVar()
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
    


class TodoList (tk.Frame):

    def __init__(self, container, list=[], onDelete = None, onDone = None):
        super().__init__(container)
        self.configure(bg ="green")
        self.ListFrame = tk.Frame(self, bg="blue")
        self.ListFrame.place(relheight=.8, relwidth=1)

        self.onDone = onDone
        self.list = list

     

        self.listbox = tk.Listbox(
            self.ListFrame,
            listvariable=self.list,
            height=6,
            selectmode='extended')

        self.listbox.pack(fill="both", expand=True)


        self.ActionsFrame = tk.Frame(self, bg="cyan")
        self.ActionsFrame.place(relheight=.2, rely=.8, relwidth=1)

        self.doneBtn = tk.Button(self.ActionsFrame, text = "Done", command=self.handleDone)
        self.doneBtn.pack(side=tk.LEFT)

        self.undoBtn = tk.Button(self.ActionsFrame, text = "Undo")
        self.undoBtn.pack(side=tk.RIGHT)


    def handleDone(self):
        if self.listbox.curselection():
            selection = self.listbox.get(self.listbox.curselection())
            self.onDone(selection)