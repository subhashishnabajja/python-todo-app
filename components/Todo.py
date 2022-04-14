
import tkinter as tk
import datetime 
from tkinter import ttk
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
        self.TodoList = TodoList(self, list= self.state["todos"], onDone = self.handleDone, onDelete = self.handleDelete)
        self.TodoList.pack(fill = "both", expand=True)

    # Function runs on todo submit
    def handleTodoText (self, text):
       
        # self.todos.set(self.state["todos"])
        # print(self.input.get())
        TODO.addTodo(text, self.state["date"].get(), datetime.datetime.now().strftime("%I:%M"))
        self.state["todos"] = TODO.getTodos(date = self.state["date"].get())
        self.TodoList.updateTreeview(list = self.state["todos"])
      

    # Function runs on date change
    def handleDateChange(self, currDate):
        # Reset to empty list
        self.state["todos"] = []

        # Update the list with fresh data
        self.state["todos"] = TODO.getTodos(date = self.state["date"].get())

        self.TodoList.updateTreeview(list = self.state["todos"])

        self.state["date"].set(currDate)


    
    # Function runs on todo is marked as done
    def handleDone(self, item):

        index = item['values'][0] - 1
    

        TODO.toggleDone(id = self.state["todos"][index][0])
        self.state["todos"] =  TODO.getTodos(date = self.state["date"].get())
        self.TodoList.updateTreeview(list = self.state["todos"])


    # Function runs when delete action is called
    def handleDelete(self, item):
        index = item['values'][0] - 1
    

        TODO.removeTodo(id = self.state["todos"][index][0])
        self.state["todos"] =  TODO.getTodos(date = self.state["date"].get())
        self.TodoList.updateTreeview(list = self.state["todos"])












