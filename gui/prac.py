from tkinter import *
from tkinter import messagebox

class MainUI():
    def __init__(self):
        global main
        global name
        main=Tk()
        name=StringVar(main,"0")
        dict={"Singh":"Singh","Aayush":"Aayush"}
        main.title("Destroy button")
        label1=Label(main,text="Escape exits").pack()
        entry1=Entry().pack()
        button1=Button(main,text="Destroy",background="blue",activebackground="white",activeforeground="black",foreground="red",command=main.destroy).pack()
        main.bind("<Escape>",self.desty)
        for (key,value) in dict.items():
            Radiobutton(main,text=key,value=value,variable=name,command=self.get_name).pack()
        main.mainloop()
    def desty(self,event):
        main.destroy()
    def get_name(self):
        messagebox.showwarning("Name ",name.get())
        label=Label(main,text=f"Welcome {name.get()}")
        label.pack()
        

        


MainUI()