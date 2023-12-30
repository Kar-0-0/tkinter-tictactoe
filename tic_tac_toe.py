import tkinter as tk
from itertools import cycle
from tkinter import messagebox

from PIL import Image, ImageTk

curr_player = "X"
place = True
ai_player = True
count = 0

print(curr_player)


def check_win():
    if (
        occupant1.get() == occupant2.get() == occupant3.get()
        and occupant1.get() != ""
        or occupant1.get() == occupant4.get() == occupant7.get()
        and occupant1.get() != ""
        or occupant4.get() == occupant5.get() == occupant6.get()
        and occupant4.get() != ""
        or occupant7.get() == occupant8.get() == occupant9.get()
        and occupant9.get() != ""
        or occupant2.get() == occupant5.get() == occupant8.get()
        and occupant2.get() != ""
        or occupant3.get() == occupant6.get() == occupant9.get()
        and occupant3.get() != ""
    ):
        window.destroy()

    elif (
        occupant1.get() == occupant5.get() == occupant9.get()
        and occupant1.get() != ""
        or occupant3.get() == occupant5.get() == occupant7.get()
        and occupant3.get() != ""
    ):
        window.destroy()
    else:
        if (
            occupant1.get() != ""
            and occupant2.get() != ""
            and occupant3.get() != ""
            and occupant4.get() != ""
            and occupant5.get() != ""
            and occupant6.get() != ""
            and occupant7.get() != ""
            and occupant8.get() != ""
            and occupant9.get() != ""
        ):
            window.destroy()


# def ai():
#     global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player, ai_player, count

#     for occupant in occupants:
#         count += 1
#         if occupant.get() == "":
#             print(f"this is the count: {count}")
#             print(f"this is the occupant: {occupant.get()}")
#             ai_marker()
#             print("I hope it is calling the function")


# def ai_marker():
#     global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player, ai_player

#     print("are we in")

#     if count == 1:
#         oes[o_count].place(x=0, y=0)
#         occupant1.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 2:
#         oes[o_count].place(x=266.6, y=0)
#         occupant2.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 3:
#         oes[o_count].place(x=533.2, y=0)
#         occupant3.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 4:
#         oes[o_count].place(x=0, y=266.6)
#         occupant4.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 5:
#         oes[o_count].place(x=266.6, y=266.6)
#         occupant5.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 6:
#         oes[o_count].place(x=533.2, y=266.6)
#         occupant6.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 7:
#         print("are we in")
#         oes[o_count].place(x=0, y=533.2)
#         occupant7.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 8:
#         oes[o_count].place(x=266.6, y=533.2)
#         occupant8.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()
#     if count == 9:
#         oes[o_count].place(x=533.2, y=533.2)
#         occupant9.set("O")
#         curr_player = "X"
#         ai = False
#         o_count += 1
#         check_win()


def place_marker1(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=0, y=0)
            occupant1.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            print("Nope it a O")
            oes[o_count].place(x=0, y=0)
            occupant1.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker2(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=266.6, y=0)
            occupant2.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=266.6, y=0)
            occupant2.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker3(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=533.2, y=0)
            occupant3.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=533.2, y=0)
            occupant3.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker4(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=0, y=266.6)
            occupant4.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=0, y=266)
            occupant4.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker5(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=266.6, y=266.6)
            occupant5.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=266.6, y=266.6)
            occupant5.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker6(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=533.2, y=266.6)
            occupant6.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=533.2, y=266.6)
            occupant6.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker7(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=0, y=533.2)
            occupant7.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=0, y=533.2)
            occupant7.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker8(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=266.6, y=533.2)
            occupant8.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=266.6, y=533.2)
            occupant8.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def place_marker9(*args):
    global board, occupant1, curr_player, oes, o_count, xes, x_count, ai_player

    if click_1:
        if curr_player == "X":
            xes[x_count].place(x=533.2, y=533.2)
            occupant9.set("X")
            curr_player = "O"
            x_count += 1
            check_win()

        elif curr_player == "O":
            oes[o_count].place(x=533.2, y=533.2)
            occupant9.set("O")
            o_count += 1
            curr_player = "X"
            check_win()


def minimax():
    pass


def player_size():
    player_choose = tk.Toplevel()
    player_choose.title("How many players are there?")
    player_choose.geometry("400x400")

    single_player_button = tk.Button(player_choose, width=50, height=30)
    single_player_button.place(x=150, y=170)


window = tk.Tk()

window.geometry("800x800")
window.title("TicTacToe")

board = tk.Canvas(window, width=800, height=800)
board.place(x=-2, y=0)

x_count = 0
imgx1 = ImageTk.PhotoImage(Image.open("markers/tictacx1.png"))
imgx2 = ImageTk.PhotoImage(Image.open("markers/tictacx2.png"))
imgx3 = ImageTk.PhotoImage(Image.open("markers/tictacx3.png"))
imgx4 = ImageTk.PhotoImage(Image.open("markers/tictacx4.png"))
imgx5 = ImageTk.PhotoImage(Image.open("markers/tictacx5.png"))

finalx1 = tk.Label(board, image=imgx1)
finalx2 = tk.Label(board, image=imgx2)
finalx3 = tk.Label(board, image=imgx3)
finalx4 = tk.Label(board, image=imgx4)
finalx5 = tk.Label(board, image=imgx5)

xes = [finalx1, finalx2, finalx3, finalx4, finalx5]

o_count = 0
imgo1 = ImageTk.PhotoImage(Image.open("markers/tictaco1.png"))
imgo2 = ImageTk.PhotoImage(Image.open("markers/tictaco2.png"))
imgo3 = ImageTk.PhotoImage(Image.open("markers/tictaco3.png"))
imgo4 = ImageTk.PhotoImage(Image.open("markers/tictaco4.png"))
imgo5 = ImageTk.PhotoImage(Image.open("markers/tictaco5.png"))

finalo1 = tk.Label(board, image=imgo1)
finalo2 = tk.Label(board, image=imgo2)
finalo3 = tk.Label(board, image=imgo3)
finalo4 = tk.Label(board, image=imgo4)
finalo5 = tk.Label(board, image=imgo5)
oes = [finalo1, finalo2, finalo3, finalo4, finalo5]

occupant1 = tk.StringVar()
occupant2 = tk.StringVar()
occupant3 = tk.StringVar()
occupant4 = tk.StringVar()
occupant5 = tk.StringVar()
occupant6 = tk.StringVar()
occupant7 = tk.StringVar()
occupant8 = tk.StringVar()
occupant9 = tk.StringVar()

occupants = [
    occupant1,
    occupant2,
    occupant3,
    occupant4,
    occupant5,
    occupant6,
    occupant7,
    occupant8,
    occupant9,
]

box1 = board.create_rectangle(0, 0, 266.6, 266.6, fill="white", outline="black")
box2 = board.create_rectangle(266.6, 0, 533.2, 266.6, fill="white", outline="black")
box3 = board.create_rectangle(533.2, 0, 800, 266.6, fill="white", outline="black")
box4 = board.create_rectangle(0, 266.6, 266.6, 533.2, fill="white", outline="black")
box5 = board.create_rectangle(266.6, 266.6, 533.2, 533.2, fill="white", outline="black")
box6 = board.create_rectangle(533.2, 266.6, 800, 533.2, fill="white", outline="black")
box7 = board.create_rectangle(0, 533.2, 266.6, 800, fill="white", outline="black")
box8 = board.create_rectangle(266.6, 533.2, 533.2, 800, fill="white", outline="black")
box9 = board.create_rectangle(533.2, 533.2, 800, 800, fill="white", outline="black")

if place == True:
    click_1 = board.tag_bind(box1, "<Button-1>", place_marker1)
    click_2 = board.tag_bind(box2, "<Button-1>", place_marker2)
    click_3 = board.tag_bind(box3, "<Button-1>", place_marker3)
    click_4 = board.tag_bind(box4, "<Button-1>", place_marker4)
    click_5 = board.tag_bind(box5, "<Button-1>", place_marker5)
    click_6 = board.tag_bind(box6, "<Button-1>", place_marker6)
    click_7 = board.tag_bind(box7, "<Button-1>", place_marker7)
    click_8 = board.tag_bind(box8, "<Button-1>", place_marker8)
    click_9 = board.tag_bind(box9, "<Button-1>", place_marker9)


window.mainloop()
