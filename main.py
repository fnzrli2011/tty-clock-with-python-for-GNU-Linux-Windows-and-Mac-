from tkinter import *
import time
import sys


root = Tk()
root.title("Digital Clock")

def GetTime():
    timevariable= time.strftime("%I:%M:%S %p")
    clock.config(text=timevariable)
    clock.after(200,GetTime)

Label(root , font=('Arial',30) , text="tty-clock",bg="black",fg='green').pack()
clock = Label(root, font=("Arial",100), bg="black", fg="green")
clock.pack()

GetTime()

root.mainloop()
