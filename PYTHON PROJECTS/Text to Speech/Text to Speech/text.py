from tkinter import *
from playsound import playsound
from gtts import gTTS

window=Tk()
window.title("Text-to-speech")
window.geometry("600x300")

text_field=StringVar()
data=Entry(window,width=70,textvariable=text_field)
data.place(x=80,y=100)

def text_to_speech():
    msg=data.get()
    message_=gTTS(msg)
    message_.save("saipriya.mp3")
    playsound("saipriya.mp3")

def reset():
    text_field.set("")

def exit():
    window.destroy()


Label(window,text="Text to Speech",font="Arial 20 bold",width=20,fg="red").pack()
Label(window,text="Enter Text",font="Arial 15 bold",fg="black").place(x=40,y=40)
Button(window,text="PLAY",font="Arial",fg="black",bg="green",command=text_to_speech).place(x=50,y=180)
Button(window,text="EXIT",font="Arial",fg="black",bg="Yellow",command=exit).place(x=180,y=180)
Button(window,text="RESET",font="Arial",bg="red",fg="Black",command=reset).place(x=301,y=180)
window.mainloop()
