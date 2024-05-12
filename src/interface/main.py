from customtkinter import *

app = CTk()
app.geometry("800x600")

btn = CTkButton(master=app, text='Options', corner_radius=32)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

app.mainloop()