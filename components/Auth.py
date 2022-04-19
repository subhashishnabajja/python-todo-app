import re
import tkinter as tk
from tkinter.tix import Tree 
from database.db import USER
from tkinter import messagebox
  


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def check(email):   
    if(re.search(regex,email)):   
        return True
    else:   
        return False

user = USER()

class AuthForm(tk.Tk):

    def __init__(self):
        super().__init__()
        # Name input config
        self.nameLabel = tk.Label(self, text = "Name")
        self.nameVariable = tk.StringVar(value="")
        self.nameInput = tk.Entry(self, textvariable=self.nameVariable)

        # Email input config
        self.emailLabel = tk.Label(self, text = "Email")
        self.emailVariable = tk.StringVar(value="")
        self.emailInput = tk.Entry(self, textvariable=self.emailVariable)

        # Password input config
        self.passwordLabel = tk.Label(self, text = "Password")
        self.passwordVariable = tk.StringVar(value="")
        self.passwordInput = tk.Entry(self, textvariable=self.passwordVariable, show="*")

       

        if not user.checkUserExists():
            # Create the user
            self.title("Create vault")
            self.nameLabel.pack(fill="x")
            self.nameInput.pack(fill="x")

            self.emailLabel.pack(fill="x")
            self.emailInput.pack(fill="x")

            self.passwordLabel.pack(fill="x")
            self.passwordInput.pack(fill="x")

             # Create button
            self.createButtton = tk.Button(self, text="Create", command=self.createUser)
            self.createButtton.pack()

        else:
            # Check the user
            self.title("Login")

            self.emailLabel.pack(fill="x")
            self.emailInput.pack(fill="x")

            self.passwordLabel.pack(fill="x")
            self.passwordInput.pack(fill="x")

             # Create button
            self.loginButtton = tk.Button(self, text="Login", command=self.checkUser)
            self.loginButtton.pack()

            self.protocol("WM_DELETE_WINDOW", self.handleClose)

            

    def createUser(self):
        name = self.nameVariable.get()
        email = self.emailVariable.get()
        password = self.passwordVariable.get()
        if name != "" or email != "" or password != "":
            # Check if the give email is valid 
            if check(email):
                user.createUser(name, email, password)
                print("user created")
                self.destroy()
        
    def checkUser(self):
        name = self.nameVariable.get()
        email = self.emailVariable.get()
        password = self.passwordVariable.get()
        if name != "" or email != "" or password != "":
            if user.checkUserCredentials(email, password):
                self.destroy()
            else:
                messagebox.showerror("Error", "Invalid Password or Email")
                self.destroy()
                quit()

    def handleClose(self):
        quit()

