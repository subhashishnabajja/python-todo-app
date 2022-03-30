import tkinter as tk
import datetime 

class TodoFrame(tk.Frame):

    def __init__(self, container):
        super().__init__(container)

        self.DatePicker = DatePicker(self)
        self.DatePicker.pack(fill="both")




class DatePicker (tk.Frame):



    def __init__(self, container):
        super().__init__(container)
        self.configure(bg="red", height=50)
        
        """"
        Entry Widget Config
        """
        self.date = tk.StringVar(value = str(datetime.datetime.now().strftime("%d/%m/%y")))
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

    def handleDecrement(self):
        currState = datetime.datetime.strptime(self.date.get(), "%d/%m/%y")
        incrementedState = currState - datetime.timedelta(days = 1)
        self.date.set(str(incrementedState.strftime("%d/%m/%y")))