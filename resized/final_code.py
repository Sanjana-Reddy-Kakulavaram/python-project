import tkinter as Tk
from tkinter import *
import random
import tkinter.messagebox
from tkinter import simpledialog


count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
count2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sums = 0
call = 0
list_of_cards = ["spades", "hearts", "clubs"]
pl_score = 0
pl2_score = 0
shown_diamonds = []
turns = 0
comp_score = 0
unshown_diamonds = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
available_cBids = unshown_diamonds[:]
draw_list = []


def First_page():
    '''
    tk = Tk()
    tk.title("Diamonds")
    tk.configure(background = "coral")
    tk.geometry("800x650")

    def display_second_page():
        Second_page()
    def quit_game():
        tk.destroy()
        quit()

    quit_button = Button(tk, text = "Quit", width = 6, font = "none 15 bold", bg = "dark blue", command = quit_game)
    quit_button.place(x = 200, y = 350)

    play_button = Button(tk, text = "Play", width = 6, font = "none 15 bold", bg = "dark blue", command  = display_second_page)
    play_button.place(x = 200, y = 300)
    tk.mainloop()
    '''
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
    tk = Tk()
    tk.title("Diamonds")
    tk.geometry("950x750")
    bg = PhotoImage(file = "back.png")
    label1 = Label( tk, image = bg)
    label1.place(x = 0, y = 0)
    '''
    tk.configure(background = "dark blue")
    tk.geometry("950x750")
    '''
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
        #global list_of_cards
        #list_of_cards.remove("hearts")

        label = Label(tk, text = "", height = 4, bg = "black", fg = "yellow")
        label.grid(row = 0, column = 4)
        label1 = Label(tk, text = "", height = 4, bg = "black", fg = "yellow")
        label1.grid(row = 0, column = 5)
        
        def hearts_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_hearts()


        def display_hearts():
            is_hearts_displayed = True
            if player_number == 1:
               
                if No_of_cards > 7:
                    Label(tk, text = "\n\n\n" + player_name[0], bg = "black", fg = "Pink").grid(row = 0, column = 2)
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : hearts_card1_value(i+1)).grid(row = 1, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = player1_cards[i], command = lambda i = i: hearts_card1_value(i+1)).grid(row = 2, column = i - 7)

            else:
                global pBid
                
                #Label(tk, text = player_name[1], bg = "black", fg = "Pink").grid(row = 5, column = 2)
                if No_of_cards > 7:
                    Label(tk, text = player_name[1], bg = "black", fg = "Pink").grid(row = 5, column = 2)
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : hearts_card_value(pBid, i+1)).grid(row = 6, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: hearts_card_value(pBid, i+1)).grid(row = 7, column = i - 6)   
                
        def hearts_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            count2[Bid-2] = 1
            global sums
            sums += 1
            '''
            for i in range(13):
                if count2[i] == 1:
                    sums += 1
            '''
            
            if sums+1 == 13-len(unshown_diamonds) or (sums == 13):
                pBid = Bid
                turns += 1
                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 8)
                Label(tk, image = hearts[pBid-1], anchor = CENTER).grid(row = 4, column = 8)
                if pBid <= 7:
                    Button(tk, image = small_icon).grid(row = 1, column = pBid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 2, column = pBid-8)
            else:
                message = "you cannot bid two cards in single turn"
                tkinter.messagebox.showinfo("MESSAGE", message)
            
        def hearts_card_value(pBid, p2Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            count[pBid-2] += 1
            
            if count[pBid-2] == 1:
                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 9)
                Label(tk, image = hearts[p2Bid-1], anchor = CENTER).grid(row = 4, column = 9)
                if p2Bid <= 6:
                    Button(tk, image = small_icon).grid(row = 6, column = p2Bid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 7, column = p2Bid-7)
                
                
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
                
                    

                Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 9)
                Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 8)
                Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 10)

        


                if len(unshown_diamonds):
                    d = diamond_label()
                    shown_diamonds.append(d)
                    Display_result_of_turn(pBid, p2Bid, cBid)
                    pBid = 0

                if turns == 13:
                    Display_final_result(pl_score, pl2_score, comp_score)

            else:
                tkinter.messagebox.showinfo("MESSAGE",player_name[0] + " should select the card first")
                
        if player_number == 1:
            player1_cards = hearts[:]
            hearts_loop()

        else:
            player2_cards = hearts[:]
            hearts_loop()
        


    def clubs_button_selected(player_number):
        #global list_of_cards
        #list_of_cards.remove("clubs")

        label = Label(tk, text = "",height = 4, bg = "black", fg = "yellow")
        label.grid(row = 0, column = 4)
        label1 = Label(tk, text = "", height = 4, bg = "black", fg = "yellow")
        label1.grid(row = 0, column = 5)

        def clubs_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_clubs()


        def display_clubs():
            is_clubs_displayed = True
            
            if player_number == 1:
                
                
                #Label(tk, text = "\n\n\nplayer-1", bg = "black", fg = "Pink").grid(row = 0, column = 2)
                if No_of_cards > 7:
                    
                    Label(tk, text = "\n\n\n" + player_name[0], bg = "black", fg = "Pink").grid(row = 0, column = 2)
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : clubs_card1_value(i+1)).grid(row = 1, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = player1_cards[i], command = lambda i = i: clubs_card1_value(i+1)).grid(row = 2, column = i - 7)
            else:
                global pBid
                
                #Label(tk, text = "player-2", bg = "black", fg = "Pink").grid(row = 5, column = 2)
                if No_of_cards > 7:
                    Label(tk, text = player_name[1], bg = "black", fg = "Pink").grid(row = 5, column = 2)
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : clubs_card_value(pBid, i+1)).grid(row = 6, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: clubs_card_value(pBid, i+1)).grid(row = 7, column = i - 6)
                
                   

        def clubs_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            count2[Bid-2] = 1
            global sums
            sums += 1
            '''
            for i in range(13):
                if count2[i] == 1:
                    sums += 1
            '''
            
            if sums+1 == 13-len(unshown_diamonds) or (sums == 13):
                pBid = Bid
                turns += 1
                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 8)
                Label(tk, image =clubs[pBid-1], anchor = CENTER).grid(row = 4, column = 8)
                if pBid <= 7:
                    Button(tk, image = small_icon).grid(row = 1, column = pBid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 2, column = pBid-8)

            else:
                message = "you cannot bid two cards in single turn"
                tkinter.messagebox.showinfo("MESSAGE", message)

        def clubs_card_value(pBid, p2Bid):

            global pl_score
            global turns
            global comp_score
            global pl2_score
            count[pBid-2] += 1

            if count[pBid-2] == 1:

                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 9)
                Label(tk, image =clubs[p2Bid-1], anchor = CENTER).grid(row = 4, column = 9)
                if p2Bid <= 6:
                    Button(tk, image = small_icon).grid(row = 6, column = p2Bid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 7, column = p2Bid-7)
                
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
                
                    

                Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 9)
                Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 8)
                Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 10)

                if len(unshown_diamonds):
                    d = diamond_label()
                    shown_diamonds.append(d)
                    Display_result_of_turn(pBid, p2Bid, cBid)
                    pBid = 0

                if turns == 13:
                    Display_final_result(pl_score, pl2_score, comp_score)

            else:
                tkinter.messagebox.showinfo("MESSAGE", player_name[0] + " should select the card first")
                    
        if player_number == 1:
            player1_cards = clubs[:]
            clubs_loop()

        else:
            player2_cards = clubs[:]
            clubs_loop()

    
    def spades_button_selected(player_number):
        #global list_of_cards
        #list_of_cards.remove("spades")

        label = Label(tk, text = "", height = 4, bg = "black", fg = "yellow")
        label.grid(row = 0, column = 4)
        label1 = Label(tk, text = "", height = 4, bg = "black", fg = "yellow")
        label1.grid(row = 0, column = 5)
        
        def spades_loop():
            global shown_diamonds
            d = diamond_label()
            shown_diamonds.append(d)
            display_spades()

        def display_spades():
            is_spades_displayed = True
            if player_number == 1:               
                        
                #Label(tk, text = "\n\n\nplayer-1", bg = "black", fg = "Pink").grid(row = 0, column = 2)
                if No_of_cards > 7:
                    Label(tk, text = "\n\n\n" + player_name[0], bg = "black", fg = "Pink").grid(row = 0, column = 2)
                    for i in range(7):
                        Button(tk, image = player1_cards[i], command = lambda i = i : spades_card1_value(i+1)).grid(row = 1, column = i )
                    for i in range(7, No_of_cards):
                        Button(tk, image = player1_cards[i], command = lambda i = i: spades_card1_value(i+1)).grid(row = 2, column = i - 7)
            else:
                global pBid
                #Label(tk, text = "player-2", bg = "black", fg = "Pink").grid(row = 5, column = 2)
                if No_of_cards > 7:
                    Label(tk, text = player_name[1], bg = "black", fg = "Pink").grid(row = 5, column = 2)
                    for i in range(6):
                        Button(tk, image = player2_cards[i], command = lambda i = i : spades_card_value(pBid, i+1)).grid(row = 6, column = i)
                    for i in range(6, No_of_cards):
                        Button(tk, image = player2_cards[i], command = lambda i = i: spades_card_value(pBid, i+1)).grid(row = 7, column = i - 6)
                           
        def spades_card1_value(Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            global pBid
            count2[Bid-2] = 1
            global sums
            sums += 1
            '''
            for i in range(13):
                if count2[i] == 1:
                    sums += 1
            '''
            
            if sums+1 == 13-len(unshown_diamonds) or (sums == 13):
                pBid = Bid
                turns += 1
                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[0] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 8)
                Label(tk, image =spades[Bid-1], anchor = CENTER).grid(row = 4, column = 8)
                if Bid <= 7:
                    Button(tk, image = small_icon).grid(row = 1, column = pBid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 2, column = pBid-8)

            else:
                message = "you cannot bid two cards in single turn"
                tkinter.messagebox.showinfo("MESSAGE", message)
            
        def spades_card_value(pBid, p2Bid):
            global pl_score
            global turns
            global comp_score
            global pl2_score
            count[pBid-2] += 1
            
            if count[pBid-2] == 1:
                #label = Label(tk, text = "Your\n Bid", bg = "forest green", fg = "black")
                label = Label(tk, text = player_name[1] + "'s Bid", bg = "black", fg = "yellow")
                label.grid(row = 2, column = 9)
                Label(tk, image =spades[p2Bid-1], anchor = CENTER).grid(row = 4, column = 9)
                if p2Bid <= 6:
                    Button(tk, image = small_icon).grid(row = 6, column = p2Bid-1)
                else:
                    Button(tk, image = small_icon).grid(row = 7, column = p2Bid-7)
                
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
               
                

                Label(tk, text = player_name[1] + "'s\n Score : \n" + str(pl2_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 9)
                Label(tk, text = player_name[0] + "'s\n Score : \n" + str(pl_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 8)
                Label(tk, text = "Computer's\n Score : \n" + str(comp_score), bg = "black", fg = "pink", font = "none 13 bold").grid(row = 6, column = 10)
            
                if len(unshown_diamonds):
                    d = diamond_label()
                    shown_diamonds.append(d)
                    Display_result_of_turn(pBid, p2Bid, cBid)
                    pBid = 0

                if turns == 13:
                    Display_final_result(pl_score, pl2_score, comp_score)

            else:
                tkinter.messagebox.showinfo("MESSAGE", player_name[0] + " should select the card first")
                    
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
        Label(tk, text = "Diamond", bg = "black", fg = "yellow").grid(row = 3, column = 6)
        Label(tk, image = diamond_shownup, anchor = CENTER).grid(row = 4, column = 6)
        Label(tk, text = "Bid-to-win", bg = "black", fg = "yellow").grid(row = 5, column = 6)
        return diamond_number

    def computer_display():
        global available_cBids
        cBid = random.choice(available_cBids)
        available_cBids.remove(cBid)
        cBid_card = spades[cBid - 2]
        Label(tk, text = "Computer-1\nbid", bg = "black", fg = "yellow").grid(row = 2, column = 10)
        Label(tk, image = cBid_card).grid(row = 4, column = 10)
        return cBid

    
    def Display_result_of_turn(pbid, p2bid, comp_bid):
        mxbid = signum(pbid, p2bid, comp_bid)
         
        if mxbid == pbid and mxbid == p2bid and mxbid == comp_bid:
            result_of_the_turn = "IT'S a Tie Between all three players"
        elif mxbid == pbid and mxbid == p2bid:
            result_of_the_turn = "IT's a tie between " + player_name[0] + " and " + player_name[1]
        elif mxbid == pbid and mxbid == comp_bid:
            result_of_the_turn = "It's a tie between " + player_name[0] + " and computer\n"
        elif mxbid == p2bid and mxbid == comp_bid:
            result_of_the_turn = "!IT'S a tie between " + player_name[1] + " and computer\n"
        elif mxbid == pbid:
            result_of_the_turn = player_name[0] + " won the diamond!!"
        elif mxbid == p2bid:
            result_of_the_turn = player_name[1] + " won the bid!!"
        else:
            result_of_the_turn = "Computer won the bid!!"
        
        tkinter.messagebox.showinfo("RESULT OF TURN", result_of_the_turn)

    def Display_final_result(pl_score, pl2_score, comp_score):
        mx = signum(pl_score, pl2_score, comp_score)
        if mx == pl_score and mx == pl2_score and mx == comp_score:
            tkinter.messagebox.showinfo("RESULT", "IT'S a Tie Between all three players\n" + player_name[0] + " score = " + player_name[1] + " score = computer score = " + str(pl_score))
        elif mx == pl_score and mx == pl2_score:
            tkinter.messagebox.showinfo("RESULT", "IT's a tie between" + player_name[0] + "and" + player_name[1] + "\n" + player_name[0] + "and" + player_name[1] + "score = " + str(pl_score) + "\ncomputer score =  " + str(comp_score))
        elif mx == pl_score and mx == comp_score:
            tkinter.messagebox.showinfo("RESULT", "IT's a tie between " + player_name[0] + " and computer\n" + player_name[0] + " and computer score = " + str(pl_score) + "\nplayer-2 score =  " + str(pl2_score))
        elif mx == pl2_score and mx == comp_score:
            tkinter.messagebox.showinfo("RESULT", "IT's a tie between " + player_name[1] + " and computer\n" + player_name[1] + " and computer- score = " + str(pl2_score) + "\nplayer-1 score =  " + str(pl_score))
        elif mx == pl_score:
            tkinter.messagebox.showinfo("RESULT", Player_name[0] + " won the game!!!\n" + player_name[0] + " score = " + str(pl_score) + "\n" + player_name[1] + " score = " + str(pl2_score) + "\ncomputer score = " + str(comp_score))
        elif mx == pl2_score:
            tkinter.messagebox.showinfo("RESULT", player_name[1] + " won the game!!\n" + player_name[1] + " score = " + str(pl2_score) + "\n" + player_name[0] + " score = " + str(pl_score) + "\ncomputer score = " + str(comp_score))
        else:
            tkinter.messagebox.showinfo("RESULT", "Computer won the game!!\n\ncomputer score = " + str(comp_score) + "\n" + player_name[0] + " score = " + str(pl_score) + "\n" + player_name[1] + " score = " + str(pl2_score))
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

    player_name = [" ", " "]
    #player_bid = [0,0]
    for i in range(0,2):
        player_name[i] = Ask_player_name(i)
    
      
    lst = [1, 2, 3]
    x = random.choice(lst)
    lst.remove(x)
    y = random.choice(lst)
    pBid = 0
    if x == 1:
        if y == 2:
            spades_button_selected(1)
            hearts_button_selected(2)
        else:
            spades_button_selected(1)
            clubs_button_selected(2)
    elif x == 2:
        if y == 1:
            hearts_button_selected(1)
            spades_button_selected(2)
        else:
            hearts_button_selected(1)
            clubs_button_selected(2)
    else:
        if y == 1:
            clubs_button_selected(1)
            spades_button_selected(2)
        else:
            clubs_button_selected(1)
            hearts_button_selected(2)


    tk.mainloop()


#First_page()
Second_page()



























