import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk

curr_player = "X"


def place_marker1(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=0, y=0)
            occupant1.set("X")
            curr_player == "O"
            x_count += 1
        elif curr_player == "O":
            oes[o_count].place(x=0, y=0)
            occupant1.set("O")
            o_count += 1
            curr_player = "X"


def place_marker2(*args):
    global board
    global occupant1
    global curr_player

    if click_2:
        if curr_player == "X":
            finalx.place(x=266.6, y=0)
            occupant2.set("X")
            curr_player == "O"
        elif curr_player == "O":
            finalo.place(x=266.6, y=0)
            occupant2.set("O")

            curr_player = "X"


window = tk.Tk()

window.geometry("800x800")
window.title("TicTacToe")

board = tk.Canvas(window, width=800, height=800)
board.place(x=-2, y=0)
x_count = 0
imgx = ImageTk.PhotoImage(Image.open("markers/tictacx.png"))
finalx = tk.Label(board, image=imgx)
xes = [finalx] * 9

o_count = 0
imgo = ImageTk.PhotoImage(Image.open("markers/tictaco.png"))
finalo = tk.Label(board, image=imgo)
oes = [finalo] * 9

occupant1 = tk.StringVar()
occupant2 = tk.StringVar()
occupant3 = tk.StringVar()
occupant4 = tk.StringVar()
occupant5 = tk.StringVar()
occupant6 = tk.StringVar()
occupant7 = tk.StringVar()
occupant8 = tk.StringVar()
occupant9 = tk.StringVar()


box1 = board.create_rectangle(0, 0, 266.6, 266.6, fill="white", outline="black")
box2 = board.create_rectangle(266.6, 0, 533.2, 266.6, fill="white", outline="black")
box3 = board.create_rectangle(533.2, 0, 800, 266.6, fill="white", outline="black")
box4 = board.create_rectangle(0, 266.6, 266.6, 533.2, fill="white", outline="black")
box5 = board.create_rectangle(266.6, 266.6, 533.2, 533.2, fill="white", outline="black")
box6 = board.create_rectangle(533.2, 266.6, 800, 533.2, fill="white", outline="black")
box7 = board.create_rectangle(0, 533.2, 266.6, 800, fill="white", outline="black")
box8 = board.create_rectangle(266.6, 533.2, 533.2, 800, fill="white", outline="black")
box9 = board.create_rectangle(533.2, 533.2, 800, 800, fill="white", outline="black")


click_1 = True if board.tag_bind(box1, "<Button-1>", place_marker1) else False
click_2 = True if board.tag_bind(box2, "<Button-3>", place_marker2) else False


window.mainloop()
