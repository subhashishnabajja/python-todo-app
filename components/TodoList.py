import tkinter as tk
from tkinter import ttk
from tkinter import messagebox



class TodoList (tk.Frame):

    def __init__(self, container, list=[], onDone = None, onDelete = None, onUpdate = None):
        super().__init__(container)

        self.ListFrame = tk.Frame(self)
        self.ListFrame.place(relheight=.8, relwidth=1)

        self.onDone = onDone
        self.onDelete = onDelete
        self.onUpdate = onUpdate
        self.list = list



        self.treeview = ttk.Treeview(
            self.ListFrame,
            columns=("No.","Time", "Status", "Description"),
            show="headings"
        )

        # Defining the heading for columns
        self.treeview.heading("No.", text="No.")
        self.treeview.heading("Time", text="Time")
        self.treeview.heading("Status", text="Status")
        self.treeview.heading("Description", text="Description")

        # Defining columns size
        self.treeview.column("No.", width=2)
        self.treeview.column("Time", width=5)
        self.treeview.column("Status", width=5)
        self.treeview.column("Description", width=400)


        # Insert todos to treeview
        self.updateTreeview(list = self.list)


        self.treeview.pack(fill="both", expand=True)


        self.ActionsFrame = tk.Frame(self)
        self.ActionsFrame.place(relheight=.2, rely=.8, relwidth=1)

        self.doneBtn = tk.Button(self.ActionsFrame, text = "Done", command=self.handleDone)
        self.doneBtn.pack(expand=True, side=tk.RIGHT)

        self.deleteBtn = tk.Button(self.ActionsFrame, text = "Delete", command=self.handleDelete)
        self.deleteBtn.pack(expand=True, side=tk.LEFT)

        self.editBtn = tk.Button(self.ActionsFrame, text = "Edit", command=self.handleUpdate)
        self.editBtn.pack(expand=True)





    def handleDone(self):
        try:
            cur = self.treeview.focus()
            
            values = self.treeview.item(cur)['values']
            self.onDone({
                "key": self.treeview.focus(),
                "values": [
                    values[0],
                    0 if values[1] == "❎" else "1",
                    values[2]
                ]
            })
        except:
            messagebox.showinfo("Info", "Please select an item")
    
        
    def handleDelete(self):
        try:
            self.onDelete(self.getCurrentSelection())
        except:
            messagebox.showinfo("Info", "Please select an item")
    
    def getCurrentSelection(self):
            cur = self.treeview.focus()
            values = self.treeview.item(cur)['values']
            print(values)
            return {
                "key": cur,
                "values": [
                    values[0],
                    values[1],
                    0 if values[2] == "❎" else 1,
                    values[3]
                ]
            }
    
    def updateTreeview(self, list = [],mode = "OVERIDE"):
        if mode == "OVERIDE":
            self.treeview.delete(*self.treeview.get_children())
          
            for i in range(len(list)):
                self.treeview.insert("", tk.END, values=(
                    i + 1,
                    list[i][3],
                    "✅" if list[i][4] == 1 else "❎" ,
                    list[i][1] 
                ))
            
    def handleUpdate(self):
        try:
            self.onUpdate(self.getCurrentSelection())
        except Exception as e:
            print(e)
            messagebox.showinfo("Info", "Please select an item")

    

