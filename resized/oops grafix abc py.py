import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import tkinter.messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image  
 
LARGEFONT = ('Helvetica',15,'bold','italic')


  
class tkinterApp(tk.Tk):
     
    # __init__ function for class Diamonds_game
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 100)
        container.grid_columnconfigure(0, weight = 100)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Page1,Rules):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
       
        def quit_game():
            controller.destroy()
            quit()
            
   
        self.canvas = tk.Canvas(self, width=950, height=800)
        self.canvas.pack()

        pil_img = Image.open("imp.png")
        self.img = ImageTk.PhotoImage(pil_img.resize((950, 800), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        button1 = ttk.Button(self, text="Start", command = lambda : controller.show_frame(Page1))
        button1_window = self.canvas.create_window(350,500,anchor = "nw", window = button1)

        button2 = ttk.Button(self, text="How to Play",command = lambda : controller.show_frame(Rules))
        button2_window = self.canvas.create_window(450,500,anchor = "nw", window = button2)

        button3 = ttk.Button(self, text="exit",command = quit_game)
        button3_window = self.canvas.create_window(550,500,anchor = "nw", window = button3)
         
         
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        self.canvas = tk.Canvas(self, width=950, height=800)
        self.canvas.pack()

        pil_img = Image.open("solid.png")
        self.img = ImageTk.PhotoImage(pil_img.resize((950, 800), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        
       
        def Continue():
            print("Continued") 

        def exit_button():
            answer = tkinter.messagebox.askquestion("Exit?", "Do you really want to exit?", icon = "warning")
            if answer == "yes":
                controller.destroy()
                exit()

        def About():
            about_the_game = "     \n\nIt is an interesting game where you need to bid on diamond card that is turned up.You can play the game until all your cards are used.For the diamond to be yours, you need to bid the higher value card than your opponents.If you bid the amount same that of your opponents, the diamond goes into the DRAW BOX.\nThis is how the game goes.Get started with the game...\n\n   "    
            tkinter.messagebox.showinfo("Diamonds", about_the_game, icon = "info")
        '''
        def newgame():
            self.destroy()
            lambda : controller.show_frame(Page1)
        '''
        menu = Menu()
        controller.config(menu = menu)
        SubMenu = Menu(menu)
        menu.add_cascade(label = "Options", menu = SubMenu)
        #SubMenu.add_command(label = "New Game", command = newgame)
        #SubMenu.add_separator()
        SubMenu.add_command(label = "Continue", command = Continue)
        SubMenu.add_command(label = "Exit", command = exit_button)
        editMenu = Menu(menu)
        menu.add_cascade(label = "Help", menu = editMenu)
        editMenu.add_command(label = "About", command = About)
    
   


class Rules(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        
        self.canvas = tk.Canvas(self, width=950, height=800)
        self.canvas.pack()

        pil_img = Image.open("rules.png")
        self.img = ImageTk.PhotoImage(pil_img.resize((950, 800), Image.ANTIALIAS))
        self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)

        #button_img = Image.open("123.png")
        #self.button_img = ImageTk.PhotoImage(button_img)
        button1 = ttk.Button(self,text = "back" ,command = lambda : controller.show_frame(StartPage))
        button1_window = self.canvas.create_window(2,2,anchor = "nw", window = button1)  
        
       


        
          
  
# Driver Code
app = tkinterApp()
app.mainloop()


