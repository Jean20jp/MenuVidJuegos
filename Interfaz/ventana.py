from tkinter import *
#import tkinter as tk
#from Snake.snake import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.window.geometry("650x550")
        self.window.title("Menu Games")
        self.window.resizable(0,0)
        self.frame = None
        self.headTitle = None
        self.btnSnake = None
        self.btnPong = None
        self.btnSpaceDfds = None
        self.btnExit = None
        self.widgetsMenu()
    
    def widgetsMenu(self):
        self.window.config(background="#09088B")
        self.frame = Frame(self.window, bg="#8A0829")
        self.frame.place(x=130,y=100,height=340,width=400)
        self.headTitle = Label(self.window, text="Menu de Juegos", 
                    font=("time new roman",20,"bold"),fg="white",bg="#09088B")
        self.headTitle.place(x=245,y=25)
        self.btnSnake = Button(self.frame,command= self.playSnake() ,text="   Snake   ",fg="black",
                    bg="white", font=("times new roman", 15))
        self.btnSnake.place(x=147,y=65)
        self.btnPong = Button(self.frame,command= None ,text="   Pong   ",fg="black",
                    bg="white", font=("times new roman", 15))
        self.btnPong.place(x=147,y=155)
        self.btnSpaceDfds= Button(self.frame,command= None ,text="   Space Defenders   ",fg="black",
                    bg="white", font=("times new roman", 15))
        self.btnSpaceDfds.place(x=100,y=255)

    def playSnake(self):
        #run()
        pass

root = Tk()
uiSystem = Menu(root)
root.mainloop()     
        