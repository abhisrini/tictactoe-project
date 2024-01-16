from tkinter import *
import random

window = Tk()


l = Label(font = ('Comic Sans', 24))
l.pack(side = 'top')

l1 = Label(font = ('Comic Sans', 24))
l1.pack(side = 'top')

pwins, cwins = 0.0, 0.0


def comp():

    game = [['', '', ''], ['', '', ''],['', '', '']]

    played = 0

    for r in range(3):

        for c in range(3):

            game[r][c] = buttons[r][c]['text']

    #print(game)

    if played == 0:

        for r in range(3):

            if game[r][0] == computer:

                if game[r][2] == computer and game[r][1] == '':

                    buttons[r][1].config(text=computer)

                    played = 1

                elif game[r][1] == computer and game[r][2] == '':

                    buttons[r][2].config(text=computer)

                    played = 1

            elif game[r][1] == computer:

                if game[r][2] == computer and game[r][0] == '':

                    buttons[r][0].config(text=computer)

                    played = 1

    if played == 0:

        for c in range(3):

            if game[0][c] == computer:

                if game[1][c] == computer and game[2][c] == '':

                    buttons[2][c].config(text=computer)

                    played = 1

            elif game[1][c] == computer:

                if game[0][c] == computer and game[2][c] == '':

                    buttons[2][c].config(text=computer)

                    played = 1

                elif game[2][c] == computer and game[0][c] == '':

                    buttons[0][c].config(text=computer)

                    played = 1

    if played == 0:

        if game[1][1] == computer:

            if game[0][0] == computer and game[2][2] == '':

                buttons[2][2].config(text=computer)

                played = 1

            elif game[2][2] == computer and game[0][0] == '':

                buttons[0][0].config(text=computer)

                played = 1

            elif game[0][2] == computer and game[2][0] == '':

                buttons[2][0].config(text=computer)

                played = 1

            elif game[2][0] == computer and game[0][2] == '':

                buttons[0][2].config(text=computer)

                played = 1

    if played == 0:

        for r in range(3):

            if game[r][0] == player:

                if game[r][2] == player and game[r][1] == '':

                    buttons[r][1].config(text = computer)

                    played = 1

                elif game[r][1] == player and game[r][2] == '':

                    buttons[r][2].config(text = computer)

                    played = 1
            elif game[r][1] == player:

                if game[r][2] == player and game[r][0] == '':

                    buttons[r][0].config(text = computer)

                    played = 1

    if played == 0:

        for c in range(3):

            if game[0][c] == player:

                if game[1][c] == player and game[2][c] == '':

                    buttons[2][c].config(text = computer)

                    played = 1
                elif game[2][c] == player and game[1][c] == '':

                    buttons[1][c].config(text = computer)

                    played = 1

            elif game[1][c] == player:

                if game[0][c] == player and game[2][c] == '':

                    buttons[2][c].config(text = computer)

                    played = 1

                elif game[2][c] == player and game[0][c] == '':

                    buttons[0][c].config(text = computer)

                    played = 1

    if played == 0:

        if game[1][1] == player:

            if game[0][0] == player and game[2][2] == '':

                buttons[2][2].config(text=computer)

                played = 1

            elif game[2][2] == player and game[0][0] == '':

                buttons[0][0].config(text=computer)

                played = 1

            elif game[0][2] == player and game[2][0] == '':

                buttons[2][0].config(text=computer)

                played = 1

            elif game[2][0] == player and game[0][2] == '':

                buttons[0][2].config(text=computer)

                played = 1

    if played == 0:

        if game[1][1] == '':

            buttons[1][1].config(text=computer)
        else:

            p = random.choice([[0,0], [0,1], [0,2],[1,0],[1,2],[2,0],[2,1],[2,2]])
            p1,p2 = p[0],p[1]

            #print(game)

            while game[p1][p2] != '':

                p = random.choice([[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]])

                p1, p2 = p[0], p[1]

            #print(p)

            buttons[p1][p2].config(text = computer)


def turn(r, c):

    global player
    global pwins
    global cwins

    if buttons[r][c]['text'] == '' and chk_win() is False:

        buttons[r][c]['text'] = player

        if chk_win() is True:

            l.config(text = 'Player Won')

            pwins += 1

        elif chk_win() is False:

            comp()

            if chk_win() is True:

                l.config(text='Computer Won')

                cwins += 1

            elif chk_win() == 'Tie':

                l.config(text='Tie')

                pwins += 0.5
                cwins += 0.5

        else:

            l.config(text='Tie')

            pwins += 0.5
            cwins += 0.5


def chk_win():

    for r in range(3):

        if buttons[r][0]['text'] == buttons[r][1]['text'] == buttons[r][2]['text'] != '':

            buttons[r][0].config(bg = 'lightgreen')
            buttons[r][1].config(bg = 'lightgreen')
            buttons[r][2].config(bg = 'lightgreen')

            return True

    for c in range(3):

        if buttons[0][c]['text'] == buttons[1][c]['text'] == buttons[2][c]['text'] != '':

            buttons[0][c].config(bg='lightgreen')
            buttons[1][c].config(bg='lightgreen')
            buttons[2][c].config(bg='lightgreen')

            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':

        buttons[0][0].config(bg='lightgreen')
        buttons[1][1].config(bg='lightgreen')
        buttons[2][2].config(bg='lightgreen')

        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':

        buttons[2][0].config(bg='lightgreen')
        buttons[1][1].config(bg='lightgreen')
        buttons[0][2].config(bg='lightgreen')

        return True

    elif mt_spaces() is False:

        for i in range(3):

            for j in range(3):

                buttons[i][j].config(bg = 'yellow')

        return 'Tie'

    else:

        return False


def mt_spaces():

     spaces = 9

     for r in range(3):

         for c in range(3):

             if buttons[r][c]['text'] != '':

                 spaces -= 1

     if spaces == 0:

         return False

     else:

         return True


def new_game():

    global player
    global computer

    players = ['X', 'O']
    player = random.choice(players)
    players.remove(player)
    computer = players[0]

    l.config(text = '')

    for r in range(3):

        for c in range(3):

            buttons[r][c].config(bg = '#F0F0F0', text = '')

    l1.config(text = f'Computer: {cwins}, Player: {pwins}')

    #print(player)
    #print(computer)


window.title('Tic-Tac-Toe')

players = ['X', 'O']
player = random.choice(players)
players.remove(player)
computer = players[0]

l1.config(text = f'Computer: {cwins}, Player: {pwins}')


buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

reset = Button(text = 'Reset Board', font = ('Comic Sans',30), command = new_game)
reset.pack(side = 'bottom')

#q = Button(text = 'Quit', font = ('Comic Sans',30), command = quitter)
#q.pack(side = 'bottom')

frame = Frame(window)
frame.pack(side = 'top')

for i in range(3):

    for j in range(3):

        buttons[i][j] = Button(frame, text='', font = ('Comic Sans',30), width = 5, height = 2, command = lambda row = i, column = j: turn(row, column))

        buttons[i][j].grid(row = i, column = j)

window.mainloop()