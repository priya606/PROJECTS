from tkinter import Button,Label
import random
import settings
import ctypes
import sys

class Cell:
    all=[]
    cell_count_label=None
    cell_count=settings.cell_count

    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.is_opened=False
        self.is_mine_candidate=False
        self.create_button=False
        self.x=x
        self.y=y
    
    #Accessing all the methods and attributes via list
    #here we declared in __init__ bcz any initilization 
    #will start here
        Cell.all.append(self)

    def create_object_button(self,location):
        b=Button(
            location,
            width=10,
            height=3,
        
        )
        
        self.create_button=b
        #passing reference
        b.bind("<Button-1>",self.left_clicked_mine)
        b.bind("<Button-4>",self.right_clicked)
    
    @staticmethod
    def create_cell_count_label(location):
        lbl=Label(
            location,
            text=f"Cells left:{settings.cell_count}",
            height=4,
            width=12

        )
        Cell.cell_count_label=lbl
    def left_clicked_mine(self,event):
        if self.is_mine:
            self.show_mine()
            
        else:
            if self.len_surrounded_cells==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.not_show_mine()
            self.not_show_mine()

            #If Mines count is equal to the cells left count,player won
            if Cell.cell_count==settings.cell_count:
                ctypes.windll.user32.MessageBoxW(0,"Congratulations! You Won the Game!","Game Over",0)
        #Cancel left and Right click events if cell is already opened
        self.create_button.unbind("<Button-1>")
        self.create_button.unbind("<Button-4>")

    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell
    @property
    def surrounded_cells(self):
            cells=[
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1,self.y),
            self.get_cell_by_axis(self.x-1,self.y+1),
            self.get_cell_by_axis(self.x,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y-1),
            self.get_cell_by_axis(self.x+1,self.y),
            self.get_cell_by_axis(self.x+1,self.y+1),
            self.get_cell_by_axis(self.x,self.y+1),
            ]
            cells=[cell for cell in cells if cell is not None]
            return cells
    @property
    def len_surrounded_cells(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter=counter+1
        return counter


    def not_show_mine(self):
        if not self.is_opened:
            Cell.cell_count-=1
            self.create_button.configure(text=self.len_surrounded_cells)
        if Cell.cell_count_label:
            Cell.cell_count_label.configure(
            text=f"Cells Left:{Cell.cell_count}"
            )
            #If it is mine candidate,then for saftey,we should
            #configure the bg to systemcolourface
            self.create_button.configure(
                bg="SystemButtonFace"
            )
        
        self.is_opened=True

    def show_mine(self):
        self.create_button.configure(background="red")
        ctypes.windll.user32.MessageBoxW(0,"You Clicked on Mine","Game Over",0)
        sys.exit()

    def right_clicked(self,event):
        if not self.is_mine_candidate:
            self.create_button.configure(
                bg="black"
            )
            self.is_mine_candidate=True
        else:
            self.create_button.configure(
                bg="SystemButtonFace"
            )
            self.is_mine_candidate=False
    @staticmethod
    def randomized_mines():
        picked_cells=random.sample(
            Cell.all,settings.mine_cells #here we divided into quarter of the cells (36/4)
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
