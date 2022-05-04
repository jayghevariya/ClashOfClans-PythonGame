
from subprocess import call
from time import sleep, time
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
import os
from src.config import rows, cols

colorama.init()


class archer_queen():
    def __init__(self, rows, cols):
        self._xstart = 44
        self._ystart = 28
        self._kinglen = 1
        self.design = "Q"
        self._health = 3000
        self._damage = 20
        self._dbuild = 0
        self._buid = [10, 12, 14]
        self._lastInput = 'w'

    def saveDirection(self, inp):
        self._lastInput = inp

    def move_right(self, i):
        self._xstart += i

    def move_left(self, i):
        self._xstart -= i

    def move_up(self, i):
        self._ystart -= i

    def move_down(self, i):
        self._ystart += i

    def get_health(self):
        return self._health

    def get_position(self):
        return self._xstart, self._ystart

    def reduce_health(self, value):
        self._health -= value
        if self._health <= 0:
            return 1
            # os.system('clear')
        else:
            return 0

    def update_health(self, value):
        self._health = value

    def building(self):
        return self._dbuild

    def attack(self, posi, hut_array, game_bord, canon_array, townhall_array, dbuilding, ranges, hut_positions, canon_positions, wizard_array, wizard_positions, lev, initialize_bord3, initialize_bord2, Level2, Level3, keyyy, archer_array):
        x, y = None, None
        attack_position = set()
        # call(f"echo {self._lastInput} >> helloo.txt", shell=True)
        if(self._lastInput == 'w'):
            x = self._ystart-8
            y = self._xstart
        elif(self._lastInput == 's'):
            x = self._ystart+8
            y = self._xstart
        elif(self._lastInput == 'a'):
            x = self._ystart
            y = self._xstart-8
        elif(self._lastInput == 'd'):
            x = self._ystart
            y = self._xstart+8

        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                if i > 0 and i < rows - 1 and j > 0 and j < cols - 1:
                    attack_position.add(
                        posi[i][j] if posi[i][j] != "WALL" else (i, j))
        for varrr in attack_position:
            string = "WALL"
            x, y = None, None
            if type(varrr) == str:
                string = varrr
            else:
                x, y = varrr
                string = posi[x][y]
            if string.startswith("HUT"):
                index = int(string[3:]) - 1
                if (ranges == 1):
                    hut_array[index].reduce(self._damage)
                hut_array[index].reduce(self._damage)

                hut_array[index].change_colour(
                    game_bord, hut_positions[index][0], hut_positions[index][1])
                if(hut_array[index].get_hitpoints() <= 0):
                    dbuilding[0] += 1

                    if(dbuilding[0] == self._buid[lev[0]]):
                        if(lev[0] == 2):
                            os.system('clear')
                            print("VICTORY")
                        elif(lev[0] == 1):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level3(archer_array)
                            initialize_bord3(keyyy[0])
                        elif(lev[0] == 0):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level2(archer_array)
                            initialize_bord2(keyyy[0])
                    #
                    for i in range(hut_positions[index][0], hut_positions[index][0]+3):
                        for j in range(hut_positions[index][1], hut_positions[index][1] + 3):
                            game_bord.change_grid(
                                j, i, Back.BLACK + Fore.BLACK + " ")
                            posi[j][i] = " "
                            print(f"\033[{j+1};{i+1}H"+" ")
            elif string.startswith("CANON"):
                index = int(string[5:]) - 1
                if(ranges == 1):
                    canon_array[index].reduce(self._damage)
                canon_array[index].reduce(self._damage)
                canon_array[index].change_colour(
                    game_bord, canon_positions[index][0], canon_positions[index][1])
                if(canon_array[index].get_hitpoints() <= 0):
                    dbuilding[0] += 1

                    if(dbuilding[0] == self._buid[lev[0]]):

                        os.system('clear')
                        print("VICTORY")
                        print(f"{(dbuilding[0]/8)*100}"+"%")
                    for i in range(canon_positions[index][0], canon_positions[index][0]+4):
                        for j in range(canon_positions[index][1], canon_positions[index][1]+3):
                            game_bord.change_grid(
                                j, i, Back.BLACK + Fore.BLACK + " ")
                            posi[j][i] = " "
                            print(f"\033[{j+1};{i+1}H"+" ")
            elif string.startswith("WIZZ"):
                index = int(string[4:]) - 1
                if(ranges == 1):
                    wizard_array[index].reduce(self._damage)
                wizard_array[index].reduce(self._damage)
                wizard_array[index].change_colour(
                    game_bord, wizard_positions[index][0], wizard_positions[index][1])
                if(wizard_array[index].get_hitpoints() <= 0):
                    dbuilding[0] += 1

                    if(dbuilding[0] == self._buid[lev[0]]):
                        if(lev[0] == 2):
                            os.system('clear')
                            print("VICTORY")
                        elif(lev[0] == 1):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level3(archer_array)
                            initialize_bord3(keyyy[0])
                        elif(lev[0] == 0):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level2(archer_array)
                            initialize_bord2(keyyy[0])
                    for i in range(wizard_positions[index][0], wizard_positions[index][0]+4):
                        for j in range(wizard_positions[index][1], wizard_positions[index][1]+3):
                            game_bord.change_grid(
                                j, i, Back.BLACK + Fore.BLACK + " ")
                            posi[j][i] = " "
                            print(f"\033[{j+1};{i+1}H"+" ")
            elif(string == "WALL"):
                posi[x][y] = " "
                game_bord.change_grid(
                    x, y, Back.BLACK + Fore.BLACK + " ")
                print(f"\033[{x+1};{y+1}H"+" ")
            elif(string == "TOWNHALL"):
                if(ranges == 1):
                    townhall_array[0].reduce(self._damage)
                townhall_array[0].reduce(self._damage)
                townhall_array[0].change_colour(game_bord, 43, 13)
                if(townhall_array[0].get_hitpoints() <= 0):
                    dbuilding[0] += 1

                    if(dbuilding[0] == self._buid[lev[0]]):
                        if(lev[0] == 2):
                            os.system('clear')
                            print("VICTORY")
                        elif(lev[0] == 1):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level3(archer_array)
                            initialize_bord3(keyyy[0])
                        elif(lev[0] == 0):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level2(archer_array)
                            initialize_bord2(keyyy[0])
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 43, Back.BLACK + Fore.BLACK + " ")
                        posi[i][43] = " "
                        print(f"\033[{i+1};44H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 44, Back.BLACK + Fore.BLACK + " ")
                        posi[i][44] = " "
                        print(f"\033[{i+1};45H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 45, Back.BLACK + Fore.BLACK + " ")
                        posi[i][45] = " "
                        print(f"\033[{i+1};46H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 46, Back.BLACK + Fore.BLACK + " ")
                        posi[i][46] = " "
                        print(f"\033[{i+1};47H"+" ")

    def archer_queen_eagle_arrow(self, posi, hut_array, game_bord, canon_array, townhall_array, dbuilding, ranges, hut_positions, canon_positions, lev, initialize_bord3, initialize_bord2, Level2, Level3, keyyy, archer_array):
        xx, yy = None, None
        attack_position = set()
        if(self._lastInput == 'w'):
            xx = self._ystart-16
            yy = self._xstart
        elif(self._lastInput == 's'):
            xx = self._ystart+16
            yy = self._xstart
        elif(self._lastInput == 'a'):
            xx = self._ystart
            yy = self._xstart-16
        elif(self._lastInput == 'd'):
            xx = self._ystart
            yy = self._xstart+16
        if xx <= 0 or xx >= rows - 1 or yy <= 0 or yy >= cols - 1:
            return
        curr = time()
        while time() - curr < 1:
            pass
        attack_position = set()
        for i in range(xx - 4, xx + 5):
            for j in range(yy - 4, yy + 5):
                if i > 0 and i < rows - 1 and j > 0 and j < cols - 1:
                    attack_position.add(
                        (posi[i][j] if posi[i][j] != "WALL" else (i, j)))
        for varrr in attack_position:
            string = "WALL"
            x, y = None, None
            if type(varrr) == str:
                string = varrr
            else:
                x, y = varrr
                string = posi[x][y]
            if string.startswith("HUT"):
                index = int(string[3:]) - 1
                if (ranges == 1):
                    hut_array[index].reduce(self._damage)
                hut_array[index].reduce(self._damage)

                hut_array[index].change_colour(
                    game_bord, hut_positions[index][0], hut_positions[index][1])
                if(hut_array[index].get_hitpoints() <= 0):
                    dbuilding[0] += 1
                    if(dbuilding[0] == self._buid[lev[0]]):
                        os.system('clear')
                        print("VICTORY")
                        print(f"{(dbuilding[0]/8)*100}"+"%")
                    #
                    for i in range(hut_positions[index][0], hut_positions[index][0]+3):
                        for j in range(hut_positions[index][1], hut_positions[index][1] + 3):
                            game_bord.change_grid(
                                j, i, Back.BLACK + Fore.BLACK + " ")
                            posi[j][i] = " "
                            print(f"\033[{j+1};{i+1}H"+" ")
            elif string.startswith("CANON"):
                index = int(string[5:]) - 1
                if(ranges == 1):
                    canon_array[index].reduce(self._damage)
                canon_array[index].reduce(self._damage)
                canon_array[index].change_colour(
                    game_bord, canon_positions[index][0], canon_positions[index][1])
                if(canon_array[index].get_hitpoints() <= 0):
                    dbuilding[0] += 1
                    if(dbuilding[0] == self._buid[lev[0]]):
                        if(lev[0] == 2):
                            os.system('clear')
                            print("VICTORY")
                        elif(lev[0] == 1):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level3(archer_array)
                            initialize_bord3(keyyy[0])
                        elif(lev[0] == 0):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level2(archer_array)
                            initialize_bord2(keyyy[0])

                    for i in range(canon_positions[index][0], canon_positions[index][0]+4):
                        for j in range(canon_positions[index][1], canon_positions[index][1]+3):
                            game_bord.change_grid(
                                j, i, Back.BLACK + Fore.BLACK + " ")
                            posi[j][i] = " "
                            print(f"\033[{j+1};{i+1}H"+" ")
            elif(string == "WALL"):
                posi[x][y] = " "
                game_bord.change_grid(
                    x, y, Back.BLACK + Fore.BLACK + " ")
                print(f"\033[{x+1};{y+1}H"+" ")
            elif(string == "TOWNHALL"):
                if(ranges == 1):
                    townhall_array[0].reduce(self._damage)
                townhall_array[0].reduce(self._damage)
                townhall_array[0].change_colour(game_bord, 43, 13)
                if(townhall_array[0].get_hitpoints() <= 0):
                    dbuilding[0] += 1
                    if(dbuilding[0] == self._buid[lev[0]]):
                        if(lev[0] == 2):
                            os.system('clear')
                            print("VICTORY")
                        elif(lev[0] == 1):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level3(archer_array)
                            initialize_bord3(keyyy[0])
                        elif(lev[0] == 0):
                            os.system('clear')
                            lev[0] += 1
                            dbuilding[0] = 0
                            Level2(archer_array)
                            initialize_bord2(keyyy[0])
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 43, Back.BLACK + Fore.BLACK + " ")
                        posi[i][43] = " "
                        print(f"\033[{i+1};44H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 44, Back.BLACK + Fore.BLACK + " ")
                        posi[i][44] = " "
                        print(f"\033[{i+1};45H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 45, Back.BLACK + Fore.BLACK + " ")
                        posi[i][45] = " "
                        print(f"\033[{i+1};46H"+" ")
                    for i in range(13, 16):
                        game_bord.change_grid(
                            i, 46, Back.BLACK + Fore.BLACK + " ")
                        posi[i][46] = " "
                        print(f"\033[{i+1};47H"+" ")
