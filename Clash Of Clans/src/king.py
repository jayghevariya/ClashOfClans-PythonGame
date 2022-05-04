
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
import os
from src.func import *

colorama.init()


class king():
    def __init__(self, rows, cols):
        self._xstart = 44
        self._ystart = 28
        self._kinglen = 1
        self.design = "K"
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
        attack_position = ''
        if(self._lastInput == 'w'):
            attack_position = posi[self._ystart-1][self._xstart]
            x = self._ystart-1
            y = self._xstart
        elif(self._lastInput == 's'):
            attack_position = posi[self._ystart+1][self._xstart]
            x = self._ystart+1
            y = self._xstart
        elif(self._lastInput == 'a'):
            attack_position = posi[self._ystart][self._xstart-1]
            x = self._ystart
            y = self._xstart-1
        elif(self._lastInput == 'd'):
            attack_position = posi[self._ystart][self._xstart+1]
            x = self._ystart
            y = self._xstart+1

        if attack_position.startswith("HUT"):
            index = int(attack_position[3:]) - 1
            # hut_array[index].reduce
            if(ranges == 1):
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
        elif attack_position.startswith("CANON"):
            index = int(attack_position[5:]) - 1
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
        elif(attack_position == "WALL"):
            posi[x][y] = " "
            game_bord.change_grid(
                x, y, Back.BLACK + Fore.BLACK + " ")
            print(f"\033[{x+1};{y+1}H"+" ")
        elif(attack_position == "TOWNHALL"):
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
        elif attack_position.startswith("WIZZ"):
            index = int(attack_position[4:]) - 1
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
