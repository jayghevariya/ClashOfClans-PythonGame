# we have pre defined function in this file
# and also we have pre executed lines of code here

import colorama
from colorama import Fore, Back, Style
import termios
import subprocess as sp
import time
import tty
import sys
import os
from src.archer_queen import archer_queen
from src.bord import *
from src.king import king

# from src.archer_queen import archer_queen


rows = 30
cols = 90
over = 0
dbuilding = [0]

isKing = True
lev = [0]


# def switchToQueen():
#     isKing = False


game_bord = layout(rows, cols)
game_queen = archer_queen(rows, cols)
game_king = king(rows, cols)
Th = townhall()
Barb = barbarian()
Can = canon()
Wizz = wizz()
Hut = huts()
Wall = walls()
posi = ([[" " for col in range(cols)]
         for row in range(rows)])
hut_positions = [[37, 8], [37, 18], [50, 18], [50, 8], [67, 13]]
canon_positions = [[26, 13], [59, 13]]
wizz_positions = [[26, 20], [59, 20]]


hut_array = []
for i in range(5):
    hut_array.append(huts())
canon_array = []
canon_array.append(canon())
canon_array.append(canon())
wizard_array = [wizz(), wizz()]
townhall_array = []
townhall_array.append(townhall())


def Level2(archer_array):
    # canon_array.clear()
    # canon_array.append(canon())
    # canon_array.append(canon())
    canon_array.append(canon())
    canon_positions.append([26, 6])
    wizz_positions.append([59, 6])
    # wizard_array.clear()
    wizard_array.append(wizz())
    archer_array.clear()
    for cannon in canon_array:
        cannon.set_health()
    for cannon in wizard_array:
        cannon.set_health()
    for cannon in townhall_array:
        cannon.set_health()
    for cannon in hut_array:
        cannon.set_health()


def Level3(archer_array):
    canon_array.append(canon())
    canon_positions.append([66, 6])
    wizard_array.append(wizz())
    wizz_positions.append([16, 13])
    archer_array.clear()
    for cannon in canon_array:
        cannon.set_health()
    for cannon in wizard_array:
        cannon.set_health()
    for cannon in townhall_array:
        cannon.set_health()
    for cannon in hut_array:
        cannon.set_health()


def show_bord():
    output = ""
    for i in range(rows):
        for j in range(cols):
            output += game_bord.get_grid(i, j)
        output += "\n"
    output += "3000 :- KING's Health"
    # output += f"{game_king.get_health()}"
    print(output)


def makeTownHall():
    for i in range(13, 16):
        game_bord.change_grid(i, 43, Fore.GREEN + Th.design)
        posi[i][43] = "TOWNHALL"
    for i in range(13, 16):
        game_bord.change_grid(i, 46, Fore.GREEN + Th.design)
        posi[i][46] = "TOWNHALL"
    for i in range(44, 46):
        game_bord.change_grid(13, i, Fore.GREEN + Th.design)
        game_bord.change_grid(15, i, Fore.GREEN + Th.design)
        posi[13][i] = "TOWNHALL"
        posi[15][i] = "TOWNHALL"
    game_bord.change_grid(14, 44, Fore.GREEN+Th.design)
    posi[14][44] = "TOWNHALL"
    game_bord.change_grid(14, 45, Fore.GREEN+Th.design)
    posi[14][45] = "TOWNHALL"


def makeWall():
    for i in range(12, 17):
        game_bord.change_grid(i, 41, Fore.WHITE + Wall.design)
        posi[i][41] = "WALL"
        game_bord.change_grid(i, 48, Fore.WHITE + Wall.design)
        posi[i][48] = "WALL"
    for i in range(41, 48):
        game_bord.change_grid(12, i, Fore.WHITE + Wall.design)
        posi[12][i] = "WALL"
        game_bord.change_grid(16, i, Fore.WHITE + Wall.design)
        posi[16][i] = "WALL"
    # for i in range(35, 55):
    #     game_bord.change_grid(6, i, Fore.WHITE + Wall.design)
    #     posi[6][i] = "WALL"
    #     game_bord.change_grid(22, i, Fore.WHITE + Wall.design)
    #     posi[22][i] = "WALL"
    # for i in range(7, 22):
    #     game_bord.change_grid(i, 35, Fore.WHITE + Wall.design)
    #     posi[i][35] = "WALL"
    #     game_bord.change_grid(i, 54, Fore.WHITE + Wall.design)
    #     posi[i][54] = "WALL"
    # for i in range(23, 66):
    #     game_bord.change_grid(3, i, Fore.WHITE + Wall.design)
    #     posi[3][i] = "WALL"
    #     game_bord.change_grid(25, i, Fore.WHITE + Wall.design)
    #     posi[25][i] = "WALL"
    # for i in range(4, 25):
    #     game_bord.change_grid(i, 23, Fore.WHITE + Wall.design)
    #     posi[i][23] = "WALL"
    #     game_bord.change_grid(i, 65, Fore.WHITE + Wall.design)
    #     posi[i][65] = "WALL"
    # game_bord.change_grid(4,23,Back.BLACK + Fore.BLACK  + " ")
    # game_bord.change_grid(7,35,Back.BLACK + Fore.BLACK  + " ")


def makehut():
    for i in range(37, 40):
        game_bord.change_grid(8, i, Fore.GREEN + Hut.design)
        posi[8][i] = "HUT1"
        game_bord.change_grid(9, i, Fore.GREEN + Hut.design)
        posi[9][i] = "HUT1"
        game_bord.change_grid(10, i, Fore.GREEN + Hut.design)
        posi[10][i] = "HUT1"
    for i in range(37, 40):
        game_bord.change_grid(18, i, Fore.GREEN + Hut.design)
        posi[18][i] = "HUT2"
        game_bord.change_grid(19, i, Fore.GREEN + Hut.design)
        posi[19][i] = "HUT2"
        game_bord.change_grid(20, i, Fore.GREEN + Hut.design)
        posi[20][i] = "HUT2"
    for i in range(50, 53):
        game_bord.change_grid(18, i, Fore.GREEN + Hut.design)
        posi[18][i] = "HUT3"
        game_bord.change_grid(19, i, Fore.GREEN + Hut.design)
        posi[19][i] = "HUT3"
        game_bord.change_grid(20, i, Fore.GREEN + Hut.design)
        posi[20][i] = "HUT3"
    for i in range(50, 53):
        game_bord.change_grid(8, i, Fore.GREEN + Hut.design)
        posi[8][i] = "HUT4"
        game_bord.change_grid(9, i, Fore.GREEN + Hut.design)
        posi[9][i] = "HUT4"
        game_bord.change_grid(10, i, Fore.GREEN + Hut.design)
        posi[10][i] = "HUT4"
    for i in range(67, 70):
        game_bord.change_grid(13, i, Fore.GREEN + Hut.design)
        posi[13][i] = "HUT5"
        game_bord.change_grid(14, i, Fore.GREEN + Hut.design)
        posi[14][i] = "HUT5"
        game_bord.change_grid(15, i, Fore.GREEN + Hut.design)
        posi[15][i] = "HUT5"


def makewizz():
    for i in range(26, 30):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ1"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ1"
    game_bord.change_grid(21, 26, Fore.GREEN + Wizz.design)
    posi[21][26] = "WIZZ1"
    game_bord.change_grid(21, 29, Fore.GREEN + Wizz.design)
    posi[21][29] = "WIZZ1"
    game_bord.change_grid(21, 27, Fore.GREEN + Wizz.design)
    posi[21][27] = "WIZZ1"
    game_bord.change_grid(21, 28, Fore.GREEN + Wizz.design)
    posi[21][28] = "WIZZ1"

    for i in range(59, 63):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ2"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ2"
    game_bord.change_grid(21, 59, Fore.GREEN + Wizz.design)
    posi[21][59] = "WIZZ2"
    game_bord.change_grid(21, 60, Fore.GREEN + Wizz.design)
    posi[21][60] = "WIZZ2"
    game_bord.change_grid(21, 61, Fore.GREEN + Wizz.design)
    posi[21][61] = "WIZZ2"
    game_bord.change_grid(21, 62, Fore.GREEN + Wizz.design)
    posi[21][62] = "WIZZ2"


def makecanon():
    for i in range(26, 30):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON1"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON1"
    game_bord.change_grid(14, 26, Fore.GREEN + Can.design)
    posi[14][26] = "CANON1"
    game_bord.change_grid(14, 29, Fore.GREEN + Can.design)
    posi[14][29] = "CANON1"
    game_bord.change_grid(14, 27, Fore.GREEN + Can.design)
    posi[14][27] = "CANON1"
    game_bord.change_grid(14, 28, Fore.GREEN + Can.design)
    posi[14][28] = "CANON1"

    for i in range(59, 63):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON2"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON2"
    game_bord.change_grid(14, 59, Fore.GREEN + Can.design)
    posi[14][59] = "CANON2"
    game_bord.change_grid(14, 62, Fore.GREEN + Can.design)
    posi[14][62] = "CANON2"
    game_bord.change_grid(14, 60, Fore.GREEN + Can.design)
    posi[14][60] = "CANON2"
    game_bord.change_grid(14, 61, Fore.GREEN + Can.design)
    posi[14][61] = "CANON2"


def makeSpoint():
    game_bord.change_grid(13, 3, Fore.WHITE + "S")
    game_bord.change_grid(14, 3, Fore.WHITE + "S")
    game_bord.change_grid(13, 87, Fore.WHITE + "S")
    game_bord.change_grid(14, 87, Fore.WHITE + "S")
    game_bord.change_grid(15, 87, Fore.WHITE + "S")
    game_bord.change_grid(15, 3, Fore.WHITE + "S")
    game_bord.change_grid(1, 44, Fore.WHITE + "S")
    game_bord.change_grid(1, 45, Fore.WHITE + "S")
    game_bord.change_grid(1, 46, Fore.WHITE + "S")


def showKing():
    game_bord.change_grid(28, 44, Fore.WHITE + game_king.design)


def initialize_bord1(keyyy):
    makeTownHall()
    makehut()
    makeWall()
    makewizz()
    makecanon()
    makeSpoint()
    if keyyy[0] == 1:
        showQueen()
    else:
        showKing2()
    show_bord()


# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------
# ------------ LEVEL2-------------------


def show_bord2():
    output = ""
    for i in range(rows):
        for j in range(cols):
            output += game_bord.get_grid(i, j)
        output += "\n"
    output += "3000 :- KING's Health"
    # output += f"{game_king.get_health()}"
    print(output)


def makeTownHall2():
    for i in range(13, 16):
        game_bord.change_grid(i, 43, Fore.GREEN + Th.design)
        posi[i][43] = "TOWNHALL"
    for i in range(13, 16):
        game_bord.change_grid(i, 46, Fore.GREEN + Th.design)
        posi[i][46] = "TOWNHALL"
    for i in range(44, 46):
        game_bord.change_grid(13, i, Fore.GREEN + Th.design)
        game_bord.change_grid(15, i, Fore.GREEN + Th.design)
        posi[13][i] = "TOWNHALL"
        posi[15][i] = "TOWNHALL"
    game_bord.change_grid(14, 44, Fore.GREEN+Th.design)
    posi[14][44] = "TOWNHALL"
    game_bord.change_grid(14, 45, Fore.GREEN+Th.design)
    posi[14][45] = "TOWNHALL"


def makeWall2():
    for i in range(12, 17):
        game_bord.change_grid(i, 41, Fore.WHITE + Wall.design)
        posi[i][41] = "WALL"
        game_bord.change_grid(i, 48, Fore.WHITE + Wall.design)
        posi[i][48] = "WALL"
    for i in range(41, 48):
        game_bord.change_grid(12, i, Fore.WHITE + Wall.design)
        posi[12][i] = "WALL"
        game_bord.change_grid(16, i, Fore.WHITE + Wall.design)
        posi[16][i] = "WALL"
    # for i in range(35,55):
    #     game_bord.change_grid(6,i,Fore.WHITE + Wall.design)
    #     posi[6][i] = "WALL"
    #     game_bord.change_grid(22,i,Fore.WHITE + Wall.design)
    #     posi[22][i] = "WALL"
    # for i in range(7,22):
    #     game_bord.change_grid(i,35,Fore.WHITE + Wall.design)
    #     posi[i][35] = "WALL"
    #     game_bord.change_grid(i,54,Fore.WHITE + Wall.design)
    #     posi[i][54] = "WALL"
    # for i in range(23,66):
    #     game_bord.change_grid(3,i,Fore.WHITE + Wall.design)
    #     posi[3][i] = "WALL"
    #     game_bord.change_grid(25,i,Fore.WHITE + Wall.design)
    #     posi[25][i] = "WALL"
    # for i in range(4,25):
    #     game_bord.change_grid(i,23,Fore.WHITE + Wall.design)
    #     posi[i][23] = "WALL"
    #     game_bord.change_grid(i,65,Fore.WHITE + Wall.design)
    #     posi[i][65] = "WALL"
    # game_bord.change_grid(4,23,Back.BLACK + Fore.BLACK  + " ")
    # game_bord.change_grid(7,35,Back.BLACK + Fore.BLACK  + " ")


def makehut2():
    for i in range(37, 40):
        game_bord.change_grid(8, i, Fore.GREEN + Hut.design)
        posi[8][i] = "HUT1"
        game_bord.change_grid(9, i, Fore.GREEN + Hut.design)
        posi[9][i] = "HUT1"
        game_bord.change_grid(10, i, Fore.GREEN + Hut.design)
        posi[10][i] = "HUT1"
    for i in range(37, 40):
        game_bord.change_grid(18, i, Fore.GREEN + Hut.design)
        posi[18][i] = "HUT2"
        game_bord.change_grid(19, i, Fore.GREEN + Hut.design)
        posi[19][i] = "HUT2"
        game_bord.change_grid(20, i, Fore.GREEN + Hut.design)
        posi[20][i] = "HUT2"
    for i in range(50, 53):
        game_bord.change_grid(18, i, Fore.GREEN + Hut.design)
        posi[18][i] = "HUT3"
        game_bord.change_grid(19, i, Fore.GREEN + Hut.design)
        posi[19][i] = "HUT3"
        game_bord.change_grid(20, i, Fore.GREEN + Hut.design)
        posi[20][i] = "HUT3"
    for i in range(50, 53):
        game_bord.change_grid(8, i, Fore.GREEN + Hut.design)
        posi[8][i] = "HUT4"
        game_bord.change_grid(9, i, Fore.GREEN + Hut.design)
        posi[9][i] = "HUT4"
        game_bord.change_grid(10, i, Fore.GREEN + Hut.design)
        posi[10][i] = "HUT4"
    for i in range(67, 70):
        game_bord.change_grid(13, i, Fore.GREEN + Hut.design)
        posi[13][i] = "HUT5"
        game_bord.change_grid(14, i, Fore.GREEN + Hut.design)
        posi[14][i] = "HUT5"
        game_bord.change_grid(15, i, Fore.GREEN + Hut.design)
        posi[15][i] = "HUT5"


def makewizz2():
    for i in range(26, 30):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ1"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ1"
    game_bord.change_grid(21, 26, Fore.GREEN + Wizz.design)
    posi[21][26] = "WIZZ1"
    game_bord.change_grid(21, 29, Fore.GREEN + Wizz.design)
    posi[21][29] = "WIZZ1"
    game_bord.change_grid(21, 27, Fore.GREEN + Wizz.design)
    posi[21][27] = "WIZZ1"
    game_bord.change_grid(21, 28, Fore.GREEN + Wizz.design)
    posi[21][28] = "WIZZ1"

    for i in range(59, 63):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ2"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ2"
    game_bord.change_grid(21, 59, Fore.GREEN + Wizz.design)
    posi[21][59] = "WIZZ2"
    game_bord.change_grid(21, 60, Fore.GREEN + Wizz.design)
    posi[21][60] = "WIZZ2"
    game_bord.change_grid(21, 61, Fore.GREEN + Wizz.design)
    posi[21][61] = "WIZZ2"
    game_bord.change_grid(21, 62, Fore.GREEN + Wizz.design)
    posi[21][62] = "WIZZ2"

    for i in range(59, 63):
        game_bord.change_grid(6, i, Fore.GREEN + Wizz.design)
        posi[6][i] = "WIZZ3"
        game_bord.change_grid(8, i, Fore.GREEN + Wizz.design)
        posi[8][i] = "WIZZ3"
    game_bord.change_grid(7, 59, Fore.GREEN + Wizz.design)
    posi[7][59] = "WIZZ3"
    game_bord.change_grid(7, 60, Fore.GREEN + Wizz.design)
    posi[7][60] = "WIZZ3"
    game_bord.change_grid(7, 61, Fore.GREEN + Wizz.design)
    posi[7][61] = "WIZZ3"
    game_bord.change_grid(7, 62, Fore.GREEN + Wizz.design)
    posi[7][62] = "WIZZ3"


def makecanon2():
    for i in range(26, 30):
        game_bord.change_grid(6, i, Fore.GREEN + Can.design)
        posi[6][i] = "CANON3"
        game_bord.change_grid(8, i, Fore.GREEN + Can.design)
        posi[8][i] = "CANON3"
    game_bord.change_grid(7, 26, Fore.GREEN + Can.design)
    posi[7][26] = "CANON3"
    game_bord.change_grid(7, 29, Fore.GREEN + Can.design)
    posi[7][29] = "CANON3"
    game_bord.change_grid(7, 27, Fore.GREEN + Can.design)
    posi[7][27] = "CANON3"
    game_bord.change_grid(7, 28, Fore.GREEN + Can.design)
    posi[7][28] = "CANON3"

    for i in range(26, 30):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON1"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON1"
    game_bord.change_grid(14, 26, Fore.GREEN + Can.design)
    posi[14][26] = "CANON1"
    game_bord.change_grid(14, 29, Fore.GREEN + Can.design)
    posi[14][29] = "CANON1"
    game_bord.change_grid(14, 27, Fore.GREEN + Can.design)
    posi[14][27] = "CANON1"
    game_bord.change_grid(14, 28, Fore.GREEN + Can.design)
    posi[14][28] = "CANON1"

    for i in range(59, 63):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON2"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON2"
    game_bord.change_grid(14, 59, Fore.GREEN + Can.design)
    posi[14][59] = "CANON2"
    game_bord.change_grid(14, 62, Fore.GREEN + Can.design)
    posi[14][62] = "CANON2"
    game_bord.change_grid(14, 60, Fore.GREEN + Can.design)
    posi[14][60] = "CANON2"
    game_bord.change_grid(14, 61, Fore.GREEN + Can.design)
    posi[14][61] = "CANON2"


def makeSpoint2():
    game_bord.change_grid(13, 3, Fore.WHITE + "S")
    game_bord.change_grid(14, 3, Fore.WHITE + "S")
    game_bord.change_grid(13, 87, Fore.WHITE + "S")
    game_bord.change_grid(14, 87, Fore.WHITE + "S")
    game_bord.change_grid(15, 87, Fore.WHITE + "S")
    game_bord.change_grid(15, 3, Fore.WHITE + "S")
    game_bord.change_grid(1, 44, Fore.WHITE + "S")
    game_bord.change_grid(1, 45, Fore.WHITE + "S")
    game_bord.change_grid(1, 46, Fore.WHITE + "S")


def showKing2():
    game_bord.change_grid(28, 44, Fore.WHITE + game_king.design)


def showQueen():
    game_bord.change_grid(28, 44, Fore.WHITE + game_queen.design)


def initialize_bord2(keyyy):
    posi = ([[" " for col in range(cols)]
             for row in range(rows)])
    # show_bord2()
    game_bord.reset_grid()

    makeTownHall2()
    makewizz2()
    makehut2()
    makeWall2()
    makecanon2()
    makeSpoint2()
    if keyyy == 1:
        showQueen()
    else:
        showKing2()
    show_bord2()


def makewizz3():
    for i in range(26, 30):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ1"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ1"
    game_bord.change_grid(21, 26, Fore.GREEN + Wizz.design)
    posi[21][26] = "WIZZ1"
    game_bord.change_grid(21, 29, Fore.GREEN + Wizz.design)
    posi[21][29] = "WIZZ1"
    game_bord.change_grid(21, 27, Fore.GREEN + Wizz.design)
    posi[21][27] = "WIZZ1"
    game_bord.change_grid(21, 28, Fore.GREEN + Wizz.design)
    posi[21][28] = "WIZZ1"

    for i in range(59, 63):
        game_bord.change_grid(20, i, Fore.GREEN + Wizz.design)
        posi[20][i] = "WIZZ2"
        game_bord.change_grid(22, i, Fore.GREEN + Wizz.design)
        posi[22][i] = "WIZZ2"
    game_bord.change_grid(21, 59, Fore.GREEN + Wizz.design)
    posi[21][59] = "WIZZ2"
    game_bord.change_grid(21, 60, Fore.GREEN + Wizz.design)
    posi[21][60] = "WIZZ2"
    game_bord.change_grid(21, 61, Fore.GREEN + Wizz.design)
    posi[21][61] = "WIZZ2"
    game_bord.change_grid(21, 62, Fore.GREEN + Wizz.design)
    posi[21][62] = "WIZZ2"

    for i in range(59, 63):
        game_bord.change_grid(6, i, Fore.GREEN + Wizz.design)
        posi[6][i] = "WIZZ3"
        game_bord.change_grid(8, i, Fore.GREEN + Wizz.design)
        posi[8][i] = "WIZZ3"
    game_bord.change_grid(7, 59, Fore.GREEN + Wizz.design)
    posi[7][59] = "WIZZ3"
    game_bord.change_grid(7, 60, Fore.GREEN + Wizz.design)
    posi[7][60] = "WIZZ3"
    game_bord.change_grid(7, 61, Fore.GREEN + Wizz.design)
    posi[7][61] = "WIZZ3"
    game_bord.change_grid(7, 62, Fore.GREEN + Wizz.design)
    posi[7][62] = "WIZZ3"

    for i in range(16, 20):
        game_bord.change_grid(13, i, Fore.GREEN + Wizz.design)
        posi[13][i] = "WIZZ4"
        game_bord.change_grid(15, i, Fore.GREEN + Wizz.design)
        posi[15][i] = "WIZZ4"
    game_bord.change_grid(14, 16, Fore.GREEN + Wizz.design)
    posi[14][16] = "WIZZ4"
    game_bord.change_grid(14, 19, Fore.GREEN + Wizz.design)
    posi[14][19] = "WIZZ4"
    game_bord.change_grid(14, 17, Fore.GREEN + Wizz.design)
    posi[14][17] = "WIZZ4"
    game_bord.change_grid(14, 18, Fore.GREEN + Wizz.design)
    posi[14][18] = "WIZZ4"


def makecanon3():
    for i in range(26, 30):
        game_bord.change_grid(6, i, Fore.GREEN + Can.design)
        posi[6][i] = "CANON3"
        game_bord.change_grid(8, i, Fore.GREEN + Can.design)
        posi[8][i] = "CANON3"
    game_bord.change_grid(7, 26, Fore.GREEN + Can.design)
    posi[7][26] = "CANON3"
    game_bord.change_grid(7, 29, Fore.GREEN + Can.design)
    posi[7][29] = "CANON3"
    game_bord.change_grid(7, 27, Fore.GREEN + Can.design)
    posi[7][27] = "CANON3"
    game_bord.change_grid(7, 28, Fore.GREEN + Can.design)
    posi[7][28] = "CANON3"

    for i in range(66, 70):
        game_bord.change_grid(6, i, Fore.GREEN + Can.design)
        posi[6][i] = "CANON4"
        game_bord.change_grid(8, i, Fore.GREEN + Can.design)
        posi[8][i] = "CANON4"
    game_bord.change_grid(7, 66, Fore.GREEN + Can.design)
    posi[7][66] = "CANON4"
    game_bord.change_grid(7, 67, Fore.GREEN + Can.design)
    posi[7][67] = "CANON4"
    game_bord.change_grid(7, 68, Fore.GREEN + Can.design)
    posi[7][68] = "CANON4"
    game_bord.change_grid(7, 69, Fore.GREEN + Can.design)
    posi[7][69] = "CANON4"

    for i in range(26, 30):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON1"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON1"
    game_bord.change_grid(14, 26, Fore.GREEN + Can.design)
    posi[14][26] = "CANON1"
    game_bord.change_grid(14, 29, Fore.GREEN + Can.design)
    posi[14][29] = "CANON1"
    game_bord.change_grid(14, 27, Fore.GREEN + Can.design)
    posi[14][27] = "CANON1"
    game_bord.change_grid(14, 28, Fore.GREEN + Can.design)
    posi[14][28] = "CANON1"

    for i in range(59, 63):
        game_bord.change_grid(13, i, Fore.GREEN + Can.design)
        posi[13][i] = "CANON2"
        game_bord.change_grid(15, i, Fore.GREEN + Can.design)
        posi[15][i] = "CANON2"
    game_bord.change_grid(14, 59, Fore.GREEN + Can.design)
    posi[14][59] = "CANON2"
    game_bord.change_grid(14, 62, Fore.GREEN + Can.design)
    posi[14][62] = "CANON2"
    game_bord.change_grid(14, 60, Fore.GREEN + Can.design)
    posi[14][60] = "CANON2"
    game_bord.change_grid(14, 61, Fore.GREEN + Can.design)
    posi[14][61] = "CANON2"


def show_bord3():
    output = ""
    for i in range(rows):
        for j in range(cols):
            output += game_bord.get_grid(i, j)
        output += "\n"
    output += "3000 :- KING's Health"
    # output += f"{game_king.get_health()}"
    print(output)


def initialize_bord3(keyyy):
    posi = ([[" " for col in range(cols)]
             for row in range(rows)])
    # show_bord2()
    game_bord.reset_grid()

    makeTownHall2()
    makewizz3()
    makehut2()
    makeWall2()
    makecanon3()
    makeSpoint2()
    if keyyy == 1:
        showQueen()
    else:
        showKing2()
    show_bord3()
