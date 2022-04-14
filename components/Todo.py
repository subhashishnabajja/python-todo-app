from re import M
import tkinter as tk
import datetime 
from tkinter import ttk
from database import db


TODO = db.TODO()

class TodoFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        # State variables
        self.state = {"todos": TODO.getTodos(date = datetime.datetime.now().strftime("%d/%m/%y")), "date": tk.StringVar(value=datetime.datetime.now().strftime("%d/%m/%y"))}
        print(self.state["todos"])
        self.input = tk.StringVar()
        self.todos = tk.StringVar(value = self.state["todos"])
        self.undoStack = []
    

        
        # Datepicker widget
        self.DatePicker = DatePicker(self,  date = self.state["date"], onChange=self.handleDateChange)
        self.DatePicker.pack(fill="both")

        # Todo input widget
        self.TodoInput = TodoInput(self, input = self.input ,onSubmit=self.handleTodoText)
        self.TodoInput.pack(fill = "both")

        # TodoList widget
        self.TodoList = TodoList(self, list= self.state["todos"], onDone = self.handleDone)
        self.TodoList.pack(fill = "both", expand=True)

    # Function runs on todo submit
    def handleTodoText (self, text):
       
        # self.todos.set(self.state["todos"])
        # print(self.input.get())
        TODO.addTodo(text, self.state["date"].get(), datetime.datetime.now().strftime("%I:%M"))
        self.state["todos"] =[todo for todo in TODO.getTodos(date = self.state["date"].get())]
        self.TodoList.updateTreeview(list = self.state["todos"])
      

    # Function runs on date change
    def handleDateChange(self, currDate):
        # Reset to empty list
        self.state["todos"] = []
        self.todos.set([])

        # Update the list with fresh data
        self.state["todos"] = [todo for todo in TODO.getTodos(date = self.state["date"].get())]
        self.todos.set(self.state["todos"])
        self.TodoList.updateTreeview(list = self.state["todos"])

        self.state["date"].set(currDate)


    
    # Function runs on todo is marked as done
    def handleDone(self, item):
     
        index = item['values'][0] - 1
    

        TODO.toggleDone(id = self.state["todos"][index][0])
        self.state["todos"] = [todo for todo in TODO.getTodos(date = self.state["date"].get())]
        self.TodoList.updateTreeview(list = self.state["todos"])
        #currTodo = self.state["todos"][index]

        # Push the todo to undo stack
        #self.undoStack.append(currTodo)

        #self.state["todos"].remove(currTodo)
        #TODO.removeTodo(date = self.state["date"].get())
    
        #self.todos.set(self.state["todos"])










class DatePicker (tk.Frame):

    def __init__(self, container, date = None, onChange = None):
        super().__init__(container)
        # States
        self.onChange = onChange


        self.configure(bg="red", height=50)

        """"
        Entry Widget Config
        """
        self.date = date
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

    def __init__(self, container, input = None, onSubmit=None ):
        super().__init__(container)
        self.onSubmit = onSubmit
        self.todos = []
        self.configure(bg="pink", height = 70)
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
    


class TodoList (tk.Frame):

    def __init__(self, container, list=[], onDone = None):
        super().__init__(container)
        self.configure(bg ="green")
        self.ListFrame = tk.Frame(self, bg="blue")
        self.ListFrame.place(relheight=.8, relwidth=1)

        self.onDone = onDone
   
        self.list = list



        self.listbox = ttk.Treeview(
            self.ListFrame,
            columns=("No.","Time", "Status", "Description"),
            show="headings"
        )

        # Defining the heading for columns
        self.listbox.heading("No.", text="No.")
        self.listbox.heading("Time", text="Time")
        self.listbox.heading("Status", text="Status")
        self.listbox.heading("Description", text="Description")

        # Defining columns size
        self.listbox.column("No.", width=2)
        self.listbox.column("Time", width=5)
        self.listbox.column("Status", width=5)
        self.listbox.column("Description", width=400)


        # Insert todos to treeview
        self.updateTreeview(list = self.list)


        self.listbox.pack(fill="both", expand=True)


        self.ActionsFrame = tk.Frame(self, bg="cyan")
        self.ActionsFrame.place(relheight=.2, rely=.8, relwidth=1)

        self.doneBtn = tk.Button(self.ActionsFrame, text = "Done", command=self.handleDone)
        self.doneBtn.pack()



    def handleDone(self):
        try:
            cur = self.listbox.focus()
            
            values = self.listbox.item(cur)['values']
            self.onDone({
                "key": self.listbox.focus(),
                "values": [
                    values[0],
                    0 if values[1] == "❎" else "1",
                    values[2]
                ]
            })
        except:
            print("Nothing is selected")
    
        

    def updateTreeview(self, list = [],mode = "OVERIDE"):
        if mode == "OVERIDE":
            self.listbox.delete(*self.listbox.get_children())
          
            for i in range(len(list)):
                self.listbox.insert("", tk.END, values=(
                    i + 1,
                    list[i][3],
                    "✅" if list[i][4] == 1 else "❎" ,
                    list[i][1] 
                ))
            
    

    

