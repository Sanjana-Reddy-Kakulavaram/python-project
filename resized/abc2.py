import tkinter as Tk
from tkinter import *
import random
import tkinter.messagebox
from tkinter import simpledialog
from PIL import ImageTk, Image


pl_score = 0
pl2_score = 0
shown_diamonds = []
turns = 0
comp_score = 0
unshown_diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
available_cBids = unshown_diamonds[:]
draw_list = []


def First_page():
    tk = Tk()
    tk.title("Diamonds") 
    tk.geometry("1000x1000")

    bg = PhotoImage(file = "bg.png")
    label = Label(tk, image = bg)


    my_canvas = Canvas(tk, width = 950, height = 650)
    my_canvas.pack(fill = "both", expand = True)
    my_canvas.create_image(0,0, image = bg, anchor = "nw")

    my_canvas.create_text(490, 325, text = "DIAMONDS!", font = ("Helventica",100), fill = "pink")

    def display_second_page():
        Second_page()
    def quit_game():
        tk.destroy()
        quit()


    button_1 = PhotoImage(file = "pla.png")
    button_1_label = Label(image = button_1)
    button1 = Button(tk,image = button_1, command = display_second_page, borderwidth = 2)
    button1_window = my_canvas.create_window(300,500,anchor = "nw", window = button1)

    button_3 = PhotoImage(file = "exi.png")
    button_3_label = Label(image = button_3)
    button3 = Button(tk, image = button_3, command = quit_game, borderwidth = 2) 
    button3_window = my_canvas.create_window(550,500,anchor = "nw", window = button3)

    tk.mainloop()

def Second_page():
    tk = Toplevel()
    tk.title("Diamonds")
    tk.geometry("1000x1000")
    img = ImageTk.PhotoImage(Image.open("back.png").resize((1000, 1000), Image.ANTIALIAS))
    lbl = Label(tk, image=img)
    lbl.img = img  # Keep a reference in case this code put is in a function.
    lbl.place(relx=0.5, rely=0.5, anchor='center')

   
    label = Label(tk, text = "",width = 10, bg = "black")
    label.grid(row = 1, column = 7)
    def Continue():
        print("Continued") 
    def newgame():
        tk.destroy()
        Second_page()
    def exit_button():
        answer = tkinter.messagebox.askquestion("Exit?", "Do you really want to exit?", icon = "warning")
        if answer == "yes":
            tk.destroy()
            exit()
    def About():
        about_the_game = "     \n\nIt is an interesting game where you need to bid on diamond card that is turned up.You can play the game until all your cards are used.For the diamond to be yours, you need to bid the higher value card than your opponet(computer).If you bid the amount same that of the computer, the diamond goes into the DRAW BOX.The final scores will decide the winner.\nThis is how the game goes.Get started with the game...\n\n   "    
        tkinter.messagebox.showinfo("Diamonds", about_the_game, icon = "info")


    def hearts_button_selected(player_number):
        def hearts_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_hearts()


        def display_hearts():
            is_hearts_displayed = True   
            if player_number == 1:
                if No_of_cards > 7:
                    Label(tk, text = "player-1", bg = "black", fg = "Pink").grid(row = 2, column = 2)
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : hearts_card1_value(i+1)).grid(row = 5, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = "player-2", command = lambda i = i: hearts_card1_value(i+1)).grid(row = 6, column = i - 7)

            else:
                if No_of_cards > 7:
                    Label(tk, text = "player-2", bg = "black", fg = "Pink").grid(row = 8, column = 2)
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : hearts_card_value(pBid, i+1)).grid(row = 10, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: hearts_card_value(pBid, i+1)).grid(row = 11, column = i - 6)
            
        def hearts_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            pBid = Bid
            turns += 1
            label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 8)
            Label(tk, image = hearts[pBid-1], anchor = CENTER).grid(row = 3, column = 8)
            if pBid <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = pBid-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = pBid-8)
            
        def hearts_card_value(pBid, p2Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 9)
            Label(tk, image = hearts[p2Bid-1], anchor = CENTER).grid(row = 3, column = 9)
            if p2Bid <= 6:
                Button(tk, image = small_icon).grid(row = 10, column = p2Bid-1)
            else:
                Button(tk, image = small_icon).grid(row = 11, column = p2Bid-7)
            
            
            cBid = computer_display()

            pBid += 1
            p2Bid += 1
            bid = signum(pBid, p2Bid, cBid)
            if bid == pBid and bid == p2Bid and bid == cBid:
                pl_score += (shown_diamonds[-1])/3
                pl2_score += (shown_diamonds[-1])/3
                comp_score += (shown_diamonds[-1])/3
            elif bid == pBid and bid == p2Bid:
                pl_score += (shown_diamonds[-1])/2
                pl2_score += (shown_diamonds[-1])/2
            elif bid == pBid and bid == cBid:
                pl_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == p2Bid and bid == cBid:
                pl2_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == pBid:
                pl_score += shown_diamonds[-1]
            elif bid == p2Bid:
                pl2_score += shown_diamonds[-1]
            else:
                comp_score += shown_diamonds[-1]
                

            Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 9)
            Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 8)
            Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 10)

            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(pBid, p2Bid, cBid)

            if turns == 13:
                Display_final_result(pl_score, pl2_score, comp_score)
            
        if player_number == 1:
            player1_cards = hearts[:]
            hearts_loop()

        else:
            player2_cards = hearts[:]
            hearts_loop()
        


    def clubs_button_selected(player_number):

        def clubs_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_clubs()


        def display_clubs():
            is_clubs_displayed = True            
            if player_number == 1:
                Label(tk, text = "player-1", bg = "black", fg = "Pink").grid(row = 2, column = 2)
                if No_of_cards > 7:
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : clubs_card1_value(i+1)).grid(row = 5, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = player1_cards[i], command = lambda i = i: clubs_card1_value(i+1)).grid(row = 6, column = i - 7)
            else:
                Label(tk, text = "player-2", bg = "black", fg = "Pink").grid(row = 8, column = 2)
                global pBid
                if No_of_cards > 7:
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : clubs_card_value(pBid, i+1)).grid(row = 10, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: clubs_card_value(pBid, i+1)).grid(row = 11, column = i - 6)
            

        def clubs_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            pBid = Bid
            turns += 1
            label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 8)
            Label(tk, image =clubs[pBid-1], anchor = CENTER).grid(row = 3, column = 8)
            if pBid <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = pBid-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = pBid-8)

        def clubs_card_value(pBid, p2Bid):

            global pl_score
            global turns
            global comp_score
            global pl2_score
            turns += 1
            label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 9)
            Label(tk, image =clubs[p2Bid-1], anchor = CENTER).grid(row = 3, column = 9)
            if p2Bid <= 6:
                Button(tk, image = small_icon).grid(row = 10,column = p2Bid-1)
            else:
                Button(tk, image = small_icon).grid(row = 11, column = p2Bid-7)
            
            cBid = computer_display()

            pBid += 1
            p2Bid += 1
            bid = signum(pBid, p2Bid, cBid)
            if bid == pBid and bid == p2Bid and bid == cBid:
                pl_score += (shown_diamonds[-1])/3
                pl2_score += (shown_diamonds[-1])/3
                comp_score += (shown_diamonds[-1])/3
            elif bid == pBid and bid == p2Bid:
                pl_score += (shown_diamonds[-1])/2
                pl2_score += (shown_diamonds[-1])/2
            elif bid == pBid and bid == cBid:
                pl_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == p2Bid and bid == cBid:
                pl2_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == pBid:
                pl_score += shown_diamonds[-1]
            elif bid == p2Bid:
                pl2_score += shown_diamonds[-1]
            else:
                comp_score += shown_diamonds[-1]
                

            Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 9)
            Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 8)
            Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 10)

            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(pBid, p2Bid, cBid)

            if turns == 13:
                Display_final_result(pl_score, pl2_score, comp_score)
            
        if player_number == 1:
            player1_cards = clubs[:]
            clubs_loop()

        else:
            player2_cards = clubs[:]
            clubs_loop()

    
    def spades_button_selected(player_number):
        def spades_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_spades()
        def display_spades():
            is_spades_displayed = True
            if player_number == 1:
                Label(tk, text = "player-1", bg = "black", fg = "Pink").grid(row = 2, column = 2)
                if No_of_cards > 7:
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : spades_card1_value(i+1)).grid(row = 5, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = player1_cards[i], command = lambda i = i: spades_card1_value(i+1)).grid(row = 6, column = i - 7)
            else:
                Label(tk, text = "player-2", bg = "black", fg = "Pink").grid(row = 8, column = 2)
                global pBid
                if No_of_cards > 7:
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : spades_card_value(pBid, i+1)).grid(row = 10, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: spades_card_value(pBid, i+1)).grid(row = 11, column = i - 6)
                        
        def spades_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            pBid = Bid
            turns += 1
            label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 8)
            Label(tk, image =spades[Bid-1], anchor = CENTER).grid(row = 3, column = 8)
            if Bid <= 7:
                Button(tk, image = small_icon).grid(row = 5, column = pBid-1)
            else:
                Button(tk, image = small_icon).grid(row = 6, column = pBid-8)
        def spades_card_value(pBid, p2Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
            label.grid(row = 2, column = 9)
            Label(tk, image =spades[p2Bid-1], anchor = CENTER).grid(row = 3, column = 9)
            if p2Bid <= 6:
                Button(tk, image = small_icon).grid(row = 10, column = p2Bid-1)
            else:
                Button(tk, image = small_icon).grid(row = 11, column = p2Bid-7)
            
            cBid = computer_display()

            pBid += 1
            p2Bid += 1
            bid = signum(pBid, p2Bid, cBid)
            if bid == pBid and bid == p2Bid and bid == cBid:
                pl_score += (shown_diamonds[-1])/3
                pl2_score += (shown_diamonds[-1])/3
                comp_score += (shown_diamonds[-1])/3
            elif bid == pBid and bid == p2Bid:
                pl_score += (shown_diamonds[-1])/2
                pl2_score += (shown_diamonds[-1])/2
            elif bid == pBid and bid == cBid:
                pl_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == p2Bid and bid == cBid:
                pl2_score += (shown_diamonds[-1])/2
                comp_score += (shown_diamonds[-1])/2
            elif bid == pBid:
                pl_score += shown_diamonds[-1]
            elif bid == p2Bid:
                pl2_score += shown_diamonds[-1]
            else:
                comp_score += shown_diamonds[-1]
                

            Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 9)
            Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 8)
            Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 4, column = 10)

            if len(unshown_diamonds):
                d = diamond_label()
                shown_diamonds.append(d)
                Display_result_of_turn(pBid, p2Bid, cBid)

            if turns == 13:
                Display_final_result(pl_score, pl2_score, comp_score)
            
        if player_number == 1:
            player1_cards = spades[:]
            spades_loop()

        else:
            player2_cards = spades[:]
            spades_loop()

    icon = PhotoImage(file = "diamond_icon_2.png")
    small = icon.zoom(15, 15)
    small_icon = small.subsample(50, 50)

    
    def diamond_label():
        global unshown_diamonds
        diamond_number = random.choice(unshown_diamonds)
        unshown_diamonds.remove(diamond_number)
        diamond_shownup = diamonds[diamond_number - 2]
        Label(tk, text = "Diamond", bg = "black", fg = "yellow").grid(row = 7, column = 9)
        Label(tk, image = diamond_shownup, anchor = CENTER).grid(row = 8, column = 9)
        Label(tk, text = "Bid-to-win", bg = "black", fg = "yellow").grid(row = 9, column = 9)
        return diamond_number

    def computer_display():
        global available_cBids
        cBid = random.choice(available_cBids)
        available_cBids.remove(cBid)
        cBid_card = spades[cBid - 2]
        Label(tk, text = "Computer-1\nbid", bg = "black", fg = "yellow").grid(row = 2, column = 10)
        Label(tk, image = cBid_card).grid(row = 3, column = 10)
        return cBid

    
    def Display_result_of_turn(pbid, p2bid, comp_bid):
        pbid += 1
        p2bid += 1
        mxbid = signum(pbid, p2bid, comp_bid)
        if mxbid == pbid and mxbid == p2bid and mxbid == comp_bid:
            result_of_the_turn = "IT'S a Tie Between all three players"
        elif mxbid == pbid and mxbid == p2bid:
            result_of_the_turn = "IT's a tie between player-1 and player-2"
        elif mxbid == pbid and mxbid == comp_bid:
            result_of_the_turn = "It's a tie between player-1 and computer\n"
        elif mxbid == p2bid and mxbid == comp_bid:
            result_of_the_turn = "!IT'S a tie between player-2 and computer\n"
        elif mxbid == pbid:
            result_of_the_turn = "Player-1 won the diamond!!"
        elif mxbid == p2bid:
            result_of_the_turn = "player-2 won the bid!!"
        else:
            result_of_the_turn = "Computer won the bid!!"
        tkinter.messagebox.showinfo(result_of_the_turn)

    def Display_final_result(pl_score, pl2_score, comp_score):
        mx = signum(pl_score, pl2_score, comp_score)
        if mx == pl_score and mx == pl2_score and mx == comp_score:
            tkinter.messagebox.showinfo("IT'S a Tie Between all three players\nplayer-1 score = player-2 score = computer score = " + str(pl_score))
        elif mx == pl_score and mx == pl2_score:
            tkinter.messagebox.showinfo("IT's a tie between player-1 and player-2\nplayer-1 and player-2 score = " + str(pl_score) + "\ncomputer score =  " + str(comp_score))
        elif mx == pl_score and mx == comp_score:
            tkinter.messagebox.showinfo("IT's a tie between player-1 and computer\nplayer-1 and computer score = " + str(pl_score) + "\nplayer-2 score =  " + str(pl2_score))
        elif mx == pl2_score and mx == comp_score:
            tkinter.messagebox.showinfo("IT's a tie between player-2 and computer\nplayer-2 and computer- score = " + str(pl2_score) + "\nplayer-1 score =  " + str(pl_score))
        elif mx == pl_score:
            tkinter.messagebox.showinfo("Player-1 won the game!!!\nplayer-1 score = " + str(pl_score) + "\nplayer-2 score = " + str(pl2_score) + "\ncomputer score = " + str(comp_score))
        elif mx == pl2_score:
            tkinter.messagebox.showinfo("player-2 won the game!!\ncomputer score = " + str(pl2_score) + "\nplayer-1 score = " + str(pl_score) + "\ncomputer-2 score = " + str(comp_score) + "\nBetter luck next time!!!")
        else:
            tkinter.messagebox.showinfo("Computer won the game!!\ncomputerscore = " + str(comp_score) + "\nplayer-1 score = " + str(pl_score) + "\nplayer-2 score = " + str(pl2_score) +"\nBetter luck next time!!!" )
        tk.destroy()
        quit()

    def Ask_player_name(i):
        Player_name = simpledialog.askstring("Enter name of Player-", i+1, parent = tk)
        if len(Player_name) > 9 or len(Player_name) == 0:
            tkinter.messagebox.showerror("Error", "Please enter name having atleast one and lessthan 10 characters")
            Ask_player_name(i)
        return Player_name



    def signum(a, b, c):
       return max([a, b, c])


    menu = Menu(tk)
    tk.config(menu = menu)
    SubMenu = Menu(menu)
    menu.add_cascade(label = "Options", menu = SubMenu)
    SubMenu.add_command(label = "New Game", command = newgame)
    SubMenu.add_separator()
    SubMenu.add_command(label = "Continue", command = Continue)
    SubMenu.add_command(label = "Exit", command = exit_button)
    editMenu = Menu(menu)
    menu.add_cascade(label = "Help", menu = editMenu)
    editMenu.add_command(label = "About", command = About)
    
    No_of_cards = 13
    diamonds = []
    for i in range(1, No_of_cards + 1):
        card = "diamonds-" + str(i+1) + "-75.png"
        diamonds.append(PhotoImage(file = card))
    spades = []
    for i in range(1, No_of_cards + 1):
        card = "spades-" + str(i+1) + "-75.png"
        spades.append(PhotoImage(file = card))
    clubs = []
    for i in range(1, No_of_cards + 1):
        card = "clubs-" + str(i+1) + "-75.png"
        clubs.append(PhotoImage(file = card))
    hearts = []
    for i in range(1, No_of_cards + 1):
        card = "hearts-" + str(i+1) + "-75.png"
        hearts.append(PhotoImage(file = card))

        
    #list_of_cards = [spades, hearts, clubs]
    spades_button_selected(1)
    hearts_button_selected(2)

    #spades_button1 = Button(tk, text = list_of_cards[0], width = 5, font = "none 12 bold", command = spades_button_selected(1)).grid(row = 1, column = 0)
    #spades_button2 = Button(tk, text = list_of_cards[0], width = 5, font = "none 12 bold", command = spades_button_selected(2)).grid(row = 1, column = 0)
    #Label(tk, text = "Choose", bg = "dark blue", fg = "red", font = "none 15 bold").grid(row = 0, column = 0)
    #spades_button1 = Button(tk, text = "spades", width = 5, font = "none 12 bold", command = spades_button_selected(x)).grid(row = 1, column = 0)
    #hearts_button1 = Button(tk, text = "hearts", width = 5, font = "none 12 bold", command = hearts_button_selected(x)).grid(row = 1, column = 1)
    #clubs_button1 = Button(tk, text = "clubs", width = 5, font = "none 12 bold", command = clubs_button_selected(x)).grid(row = 1, column = 2)
    #hearts_button1 = Button(tk, text = "hearts", width = 5, font = "none 12 bold", command = hearts_button_selected(x)).grid(row = 1, column = 1)
    #Label(tk, text = "Diamond\nto bid", bg = "dark blue", fg = "red", width = 8, font = "none 12 bold").grid(row = 0, column = 2)
    #tkinter.messagebox.showinfo("Welcome to diamonds", "Choose the deck of cards you wanna play with...\nFor more info about the game, go to HELP\nClick OK to start the game.")
    
    #Label(tk, text = "Choose", bg = "dark blue", fg = "red", font = "none 15 bold").grid(row = 0, column = 0)
    #spades_button2 = Button(tk, text = "spades", width = 5, font = "none 12 bold", command = spades_button_selected(2)).grid(row = 2, column = 0)
    #hearts_button2 = Button(tk, text = "hearts", width = 5, font = "none 12 bold", command = hearts_button_selected(2)).grid(row = 2, column = 1)
    #clubs_button2 = Button(tk, text = "clubs", width = 5, font = "none 12 bold", command = clubs_button_selected(2)).grid(row = 2, column = 2)
    #Label(tk, text = "Diamond\nto bid", bg = "dark blue", fg = "red", width = 8, font = "none 12 bold").grid(row = 0, column = 2)
    #tkinter.messagebox.showinfo("Welcome to diamonds", "Choose the deck of cards you wanna play with...\nFor more info about the game, go to HELP\nClick OK to start the game.")

    player_name = [" ", " "]
    for i in range(0,2):
        player_name[i] = Ask_player_name(i)
        


    tk.mainloop()

First_page()
'''
def third_page():
    
    tk = Tk()
    
    list_of_cards = ["spades", "hearts", "clubs"]
    cards2 = []

    def Ask_player_name(i):
        Player_name = simpledialog.askstring("Enter name of Player-", i+1, parent = tk)
        if len(Player_name) > 9 or len(Player_name) == 0:
            tkinter.messagebox.showerror("Error", "Please enter name having atleast one and lessthan 10 characters")
            Ask_player_name(i)
        return Player_name

    
    def player_card(i, j):
        if i==1:
            l = 0
            while l < 2:
                global p1
                p1 = j
                #k = 0
                if i != j:
                    cards2.append(list_of_cards[l])
                    #k += 1
        else:
            #global p1
            if list_of_cards[p1] == "spades":
                spades_button_selected(1)
                if cards2[j] == "spades":
                    spades_button_selected(2)
                    second_page()
                elif cards2[j] == "hearts":
                    hearts_button_selected(2)
                    second_page()
                else:
                    clubs_button_selected(2)
                    second_page()
            elif list_of_cards[p1] == "hearts":
                hearts_button_selected(1)
                if cards2[j] == "spades":
                    spades_button_selected(2)
                    second_page()
                elif cards2[j] == "hearts":
                    hearts_button_selected(2)
                    second_page()
                else:
                    clubs_button_selected(2)
                    second_page()
            else:
                clubs_button_selected(1)
                if cards2[j] == "spades":
                    spades_button_selected(2)
                    second_page()
                elif cards2[j] == "hearts":
                    hearts_button_selected(2)
                    second_page()
                else:
                    clubs_button_selected(2)
                    second_page()
    def player_choice(i):
        if i == 0:
            button1 = Button(tk, text = list_of_cards[0], width = 5, font = "none 12 bold", command = player_card(1, 0)).grid(row = 1, column = 0)
            button2 = Button(tk, text = list_of_cards[1], width = 5, font = "none 12 bold", command = player_card(1, 1)).grid(row = 1, column = 0)
            button3 = Button(tk, text = list_of_cards[2], width = 5, font = "none 12 bold", command = player_card(1, 2)).grid(row = 1, column = 0)
        else:
            button1 = Button(tk, text = cards2[0], width = 5, font = "none 12 bold", command = player_card(2, 0)).grid(row = 1, column = 1)
            button2 = Button(tk, text = cards2[1], width = 5, font = "none 12 bold", command = player_card(2, 1)).grid(row = 1, column = 1)
        
        
    player_name = [" ", " "]
    #player_bid = [0,0]
    for i in range(0,2):
        player_name[i] = Ask_player_name(i)
        player_choice(i)
        
        
    tk.mainloop()

#irst_page()
#Second_page()
third_page()

'''

























