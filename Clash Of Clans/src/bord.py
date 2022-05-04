# import config
from time import sleep
from traceback import print_tb
import colorama
from colorama import Fore, Back, Style
import numpy as np
import os
import random

colorama.init()


class layout():
    def __init__(self, rows, cols):
        self._rows = rows
        self._cols = cols
        self._grid = ([[Back.BLACK + Fore.BLACK + " " for col in range(self._cols)]
                       for row in range(self._rows)])

        for val in range(self._cols):
            self._grid[0][val] = Fore.WHITE + 'X'
            self._grid[self._rows - 1][val] = Fore.GREEN + 'X'

        for val in range(self._rows):
            self._grid[val][0] = Fore.WHITE + 'X'
            self._grid[val][self._cols - 1] = Fore.WHITE + 'X'

    def get_grid(self, i, j):
        return self._grid[i][j]

    def change_grid(self, i, j, val):
        self._grid[i][j] = val

    def reset_grid(self):
        self._grid = ([[Back.BLACK + Fore.BLACK + " " for col in range(self._cols)]
                       for row in range(self._rows)])

        for val in range(self._cols):
            self._grid[0][val] = Fore.WHITE + 'X'
            self._grid[self._rows - 1][val] = Fore.GREEN + 'X'

        for val in range(self._rows):
            self._grid[val][0] = Fore.WHITE + 'X'
            self._grid[val][self._cols - 1] = Fore.WHITE + 'X'


class parent():
    def __init__(self):
        self._xlen = 3
        self._ylen = 4
        self._hitpoints = 10

    def reduce(self, value):
        self._hitpoints -= value

    def get_hitpoints(self):
        return self._hitpoints


class walls(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 1
        self._xlen = 1
        self._ylen = 1
        self.design = "▪️"

    def get_health(self):
        return self._hitpoints


class barbarian(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 1000
        self._xlen = 1
        self._ylen = 1
        self.design = "B"


class wizz(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 200
        self._xlen = 3
        self._ylen = 4
        self._damage = 10
        self.design = "W"

    def get_health(self):
        return self._hitpoints

    def set_health(self):
        self._hitpoints = 200

    def change_colour(self, game_bord, a, b):
        if(self._hitpoints > 100):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.GREEN + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+1, i, Fore.GREEN + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+2, i, Fore.GREEN + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.GREEN + self.design)
        elif(self._hitpoints > 40):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.YELLOW + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+1, i, Fore.YELLOW + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+2, i, Fore.YELLOW + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.YELLOW + self.design)
        elif(self._hitpoints > 0):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.RED + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+1, i, Fore.RED + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+2, i, Fore.RED + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.RED + self.design)

    def get_damage(self):
        return self._damage


class canon(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 200
        self._xlen = 3
        self._ylen = 4
        self._damage = 10
        self.design = "C"

    def set_health(self):
        self._hitpoints = 200

    def get_health(self):
        return self._hitpoints

    def change_colour(self, game_bord, a, b):
        if(self._hitpoints > 100):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.GREEN + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+1, i, Fore.GREEN + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+2, i, Fore.GREEN + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.GREEN + self.design)
        elif(self._hitpoints > 40):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.YELLOW + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+1, i, Fore.YELLOW + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+2, i, Fore.YELLOW + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.YELLOW + self.design)
        elif(self._hitpoints > 0):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.RED + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+1, i, Fore.RED + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+2, i, Fore.RED + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.RED + self.design)

    def get_damage(self):
        return self._damage


class townhall(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 500
        self._xlen = 3
        self._ylen = 4
        self.design = "T"

    def get_health(self):
        return self._hitpoints

    def set_health(self):
        self._hitpoints = 500

    def change_colour(self, game_bord, a, b):
        if(self._hitpoints > 250):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.GREEN + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+1, i, Fore.GREEN + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+2, i, Fore.GREEN + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.GREEN + self.design)
        elif(self._hitpoints > 100):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.YELLOW + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+1, i, Fore.YELLOW + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+2, i, Fore.YELLOW + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.YELLOW + self.design)

        elif(self._hitpoints > 0):
            for i in range(a, a+4):
                game_bord.change_grid(b, i, Fore.RED + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+1, i, Fore.RED + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+2, i, Fore.RED + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.RED + self.design)


class huts(parent):
    def __init__(self):
        super().__init__()
        self._hitpoints = 100
        self._xlen = 3
        self._ylen = 3
        self.design = "H"

    def get_health(self):
        return self._hitpoints

    def set_health(self):
        self._hitpoints = 100

    def change_colour(self, game_bord, a, b):
        if(self._hitpoints > 50):
            for i in range(a, a+3):
                game_bord.change_grid(b, i, Fore.GREEN + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+1, i, Fore.GREEN + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.GREEN + self.design)
                game_bord.change_grid(b+2, i, Fore.GREEN + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.GREEN + self.design)
        elif(self._hitpoints > 20):
            for i in range(a, a+3):
                game_bord.change_grid(b, i, Fore.YELLOW + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+1, i, Fore.YELLOW + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.YELLOW + self.design)
                game_bord.change_grid(b+2, i, Fore.YELLOW + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.YELLOW + self.design)
        elif(self._hitpoints > 0):
            for i in range(a, a+3):
                game_bord.change_grid(b, i, Fore.RED + self.design)
                print(f"\033[{b+1};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+1, i, Fore.RED + self.design)
                print(f"\033[{b+2};{i+1}H"+Fore.RED + self.design)
                game_bord.change_grid(b+2, i, Fore.RED + self.design)
                print(f"\033[{b+3};{i+1}H"+Fore.RED + self.design)


class archer:
    def __init__(self, X, Y) -> None:
        self._hitpoints = 100
        self._damage = 10
        self._x = X
        self._y = Y
        self.design = "A"
        self._buid = [10, 12, 14]
        self._dbuild = 0
        print(f"\033[{self._x + 1};{self._y + 1}H" + Fore.WHITE + self.design)

    def get_position(self):
        return self._x, self._y

    def getDamage(self):
        return self._damage

    def get_health(self):
        return self._hitpoints

    def reduce_health(self, value):
        self._hitpoints -= value
        if self._hitpoints <= 0:
            return 1
        else:
            return 0

    def move(self, posi, canon_positions, wizz_positions, hut_positions, canon_array, wizard_array, hut_array, townhall_array, ranges, game_bord, lev, dbuilding, initialize_bord3, initialize_bord2, Level2, Level3, keyyy, archer_array):
        string = ""
        dist = 10000000000
        fx, fy = self._x, self._y
        for zz in canon_positions:
            if posi[zz[1]][zz[0]] == ' ':
                continue
            index = int(posi[zz[1]][zz[0]][5:]) - 1
            if canon_array[index].get_health() <= 0:
                continue
            curr_dist = ((zz[1] - self._x)**2 + (zz[0] - self._y)**2)**0.5
            if curr_dist < dist:
                dist = curr_dist
                string = posi[zz[1]][zz[0]]
                fx, fy = zz[1], zz[0]
        for yy, xx in wizz_positions:
            if posi[xx][yy] == ' ':
                continue
            index = int(posi[xx][yy][4:]) - 1
            if wizard_array[index].get_health() <= 0:
                continue
            curr_dist = ((xx - self._x)**2 + (yy - self._y)**2)**0.5
            if curr_dist < dist:
                dist = curr_dist
                string = posi[xx][yy]
                fx, fy = xx, yy
        for yy, xx in hut_positions:
            if posi[xx][yy] == ' ':
                continue
            index = int(posi[xx][yy][3:]) - 1
            if hut_array[index].get_health() <= 0:
                continue
            curr_dist = ((xx - self._x)**2 + (yy - self._y)**2)**0.5
            if curr_dist < dist:
                dist = curr_dist
                string = posi[xx][yy]
                fx, fy = xx, yy
        if townhall_array[0].get_health() > 0:
            curr_dist = ((14 - self._x)**2 + (44 - self._y)**2)**0.5
            if curr_dist < dist:
                dist = curr_dist
                string = posi[14][44]
                fx, fy = 14, 44
        print(f"\033[35;1H{dist} {string}")
        if dist <= 6:
            self.attack(posi, string, canon_array, wizard_array, hut_array, townhall_array,
                        canon_positions, wizz_positions, hut_positions, ranges, game_bord, lev, dbuilding, initialize_bord3, initialize_bord2, Level2, Level3, keyyy, archer_array)
        else:
            fx = 0 if fx == self._x else ((fx - self._x) / abs(fx - self._x))
            fy = 0 if fy == self._y else ((fy - self._y) / abs(fy - self._y))
            print(f"\033[{int(self._x+1)};{int(self._y+1)}H" + " ")
            self._x += fx
            self._y += fy
            if posi[int(self._x)][int(self._y)] == "WALL":
                print(f"\033[{int(self._x+1)};{int(self._y+1)}H" + " ")
                # sleep(0.5)
            # print(f"\033[35;1H{int(self._x + 1)}, {self._y + 1}")
            print(f"\033[{int(self._x+1)};{int(self._y+1)}H" +
                  Fore.WHITE + self.design)

    def attack(self, posi,  string, canon_array, wizard_array, hut_array, townhall_array,
               canon_positions, wizard_positions, hut_positions, ranges, game_bord, lev, dbuilding, initialize_bord3, initialize_bord2, Level2, Level3, keyyy, archer_array):
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
                        Level3(archer_array)
                        initialize_bord3(keyyy[0])
                    elif(lev[0] == 0):
                        os.system('clear')
                        lev[0] += 1
                        dbuilding[0] = 0
                        Level2(archer_array)
                        initialize_bord2(keyyy[0])
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
