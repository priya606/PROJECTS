from tkinter import *
import random

windows=Tk()
windows.title("DICE-SIMULATOR GAME")
windows.geometry("400x300")
windows.configure(bg="black")

def dice_simulator():
    dices=['\u2680', '\u2681','\u2682', '\u2683','\u2684', '\u2685']
    b.configure(text=f"{random.choice(dices)}{random.choice(dices)}")
    b.pack()

b=Label(windows,bg="yellow",fg="white",font=("times",250))
a=Button(windows,text="ROLL",bg="violet",fg="white",height=1,width=6,command=dice_simulator)
a.pack(padx=5,pady=6)
windows.mainloop()