import datetime
import tkinter as tk

class DatePicker (tk.Frame):

    def __init__(self, container, date = None, onChange = None):
        super().__init__(container)
        # States
        self.onChange = onChange


        self.configure( height=50)

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


