from customtkinter import *
import customtkinter
from time import sleep
from delArqsExplorer import delArqsExplorer
from layoutConsole import layout
from clearConsole import clearConsole
from clearArqTemp import clearArqTemps
from cleanDisk import cleanDisk
from esvaziarLixeira import esvaziarLixeira
from getUser import *
from validarOptionUser import *

class App(CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = CTkTextbox(master=self, height=600 ,width=500, corner_radius=10)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Manager SystemPy")
    
    def cleanTemps():
       clearArqTemps()
       
    def cleanDisk():
      cleanDisk()
       
    def cleanPath():
       delArqsExplorer()

    def cleanTrash():
       esvaziarLixeira()

    def viewIpv4():
       andressLocalHost()
    
    def exitProgram():
       exit()

App = App

app = App()

button = CTkButton(master=app, text="CTkButton", command=App.cleanTemps)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
button = CTkButton(master=app, text="CTkButton", command=App.cleanDisk)
button.place(relx=1, rely=1, anchor=customtkinter.CENTER)
button = CTkButton(master=app, text="CTkButton", command=App.cleanPath)
button.place(relx=1.5, rely=1.5, anchor=customtkinter.CENTER)
button = CTkButton(master=app, text="CTkButton", command=App.cleanTrash)
button.place(relx=2, rely=2, anchor=customtkinter.CENTER)
button = CTkButton(master=app, text="CTkButton", command=App.viewIpv4)
button.place(relx=2.5, rely=2.5, anchor=customtkinter.CENTER)
button = CTkButton(master=app, text="CTkButton", command=App.exitProgram)
button.place(relx=3, rely=3, anchor=customtkinter.CENTER)

app.mainloop()