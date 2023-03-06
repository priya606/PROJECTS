from tkinter import *
import settings
import utils
from cell import Cell

root=Tk()
root.geometry("1000x500")
root.title("Minesweeper Game")
root.resizable("False","False")
root.configure(background="Black")

#Labelling
top_frame=Frame(
    root,
    background="red",
    width=settings.width,
    height=utils.height_percentage(25)
)
top_frame.place(x=0,y=0)
game_title=Label(
    top_frame,
    background="black",
    fg="white",
    text="Minesweeper Game",
    font=("",40)
)
game_title.place(
    x=utils.width_percentage(25),y=0
    
)

left_frame=Frame(
    root,
    background="blue",
    width=utils.width_percentage(25),
    height=utils.height_percentage(75)
)
left_frame.place(x=0,y=utils.height_percentage(25))

right_frame=Frame(
    root,
    background="green",
    height=utils.height_percentage(75),
    width=utils.width_percentage(75)
)
right_frame.place(x=utils.width_percentage(25),y=utils.height_percentage(25))

#creating buttons
for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c=Cell(x,y)
        c.create_object_button(right_frame)
        c.create_button.grid(
            row=x,column=y
        )
#Call the label from cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label.place(x=0,y=0)

Cell.randomized_mines()
root.mainloop()