
from cgitb import text
import tkinter as tk
import datetime 
from tkinter import ttk
from turtle import update
from database import db

# Components 
from components.TodoInput import TodoInput
from components.Datepicker import DatePicker
from components.TodoList import TodoList


TODO = db.TODO()

class TodoFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # State variables
        self.state = {"todos": TODO.getTodos(date = datetime.datetime.now().strftime("%d/%m/%y")), "date": tk.StringVar(value=datetime.datetime.now().strftime("%d/%m/%y"))}
        print(self.state["todos"])
        self.input = tk.StringVar()
    

        
        # Datepicker widget
        self.DatePicker = DatePicker(self,  date = self.state["date"], onChange=self.handleDateChange)
        self.DatePicker.pack(fill="both")

        # Todo input widget
        self.TodoInput = TodoInput(self, input = self.input ,onSubmit=self.handleTodoText)
        self.TodoInput.pack(fill = "both")

        # TodoList widget
        self.TodoList = TodoList(self, list= self.state["todos"], onDone = self.handleDone, onDelete = self.handleDelete, onUpdate=self.handleUpdate)
        self.TodoList.pack(fill = "both", expand=True)

    # Update list method
    def updateList(self):
        self.state["todos"] = TODO.getTodos(self.state["date"].get())
        self.TodoList.updateTreeview(list = self.state["todos"])


    # Function runs on todo submit
    def handleTodoText (self, text):
       
        # self.todos.set(self.state["todos"])
        # print(self.input.get())
        TODO.addTodo(text, self.state["date"].get(), datetime.datetime.now().strftime("%I:%M"))
        self.updateList()
      

    # Function runs on date change
    def handleDateChange(self, currDate):
        # Reset to empty list
        self.state["todos"] = []

        # Update the list with fresh data
        self.updateList()

        self.state["date"].set(currDate)


    
    # Function runs on todo is marked as done
    def handleDone(self, item):

        index = item['values'][0] - 1
    

        TODO.toggleDone(id = self.state["todos"][index][0])
        self.updateList()


    # Function runs when delete action is called
    def handleDelete(self, item):
        index = item['values'][0] - 1
    

        TODO.removeTodo(id = self.state["todos"][index][0])
        self.updateList()

    # Function runs when update function is run
    def handleUpdate(self, item):
        


        print(item)
        toplevel = tk.Toplevel()
        toplevel.geometry("250x100")
        textVariable = tk.StringVar(value=item["values"][3])
        textEntry = tk.Entry(toplevel, textvariable=textVariable, font=('Arial 14'))
        textEntry.pack(fill="x", expand=True)
        def eventHandler():
            TODO.updateTodo(id = item["values"][0], text=item["values"][3], newText=textVariable.get())
            toplevel.destroy()
            self.updateList()


        updateButton = tk.Button(toplevel, text = "Update" , command=eventHandler)
        updateButton.pack(expand=True, side=tk.RIGHT)

    











