from operator import ne
import colorama
from colorama import Fore, Back, Style
import termios
import subprocess as sp
import time
import tty
import sys
import os
import signal
from src.archer_queen import archer_queen
from src.bord import *
from src.func import *
from src.input import *
from src.config import *
from src.king import *

archer_array=[]
keyyy = [-1]
list = os.listdir("replays")
number_files = len(list)
open(f'replays/{number_files + 1}.txt', 'w').close()
ranges = 0

file = open(f'replays/{number_files + 1}.txt', 'w')

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    os.system("clear")
    inputs = Get()
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    inputt = input("Press 1 to choose archer queen or 0 to choose king: ")
    keyyy[0] = int(inputt)
    # print(inputt , type(inputt))
    if keyyy[0] == 1:
        game_king = game_queen
    os.system('clear')
    initialize_bord1(keyyy)

    # while keyyy != 1 and keyyy != 0:
    #         keyyy = int(inputt)
    #     inputt = input("Press 1 to choose archer queen or 0 to choose king: ")
    #     if inputt == "1" or inputt == "0":
    #         if keyyy == 1:
    #             # isKing = False
    #             game_king = game_queen
    # print(game_king)
    # exit(0)
    
    while(1):
        # print("\033[35;1H")

        # for cannon in canon_array:
        #     if cannon

        inp = input_to(inputs)
        # inp= inputs.__call__()
        if(inp == None):
            file.write("-\n")
        else:
            file.write(inp)
            file.write("\n")
        if inp == "1":
            archer_array.append(archer(14, 4))
        elif inp == "2":
            archer_array.append(archer(2, 45))
        elif inp == "3":
            archer_array.append(archer(14, 86))
        for arch in archer_array:
            if arch.get_health() > 0:
                arch.move(posi, canon_positions, wizz_positions, hut_positions,
                          canon_array, wizard_array, hut_array, townhall_array, ranges, game_bord,lev,dbuilding,initialize_bord3,initialize_bord2,Level2,Level3,keyyy,archer_array)
        for cann_coords in canon_positions:
            cx, cy = cann_coords[0], cann_coords[1]
            # print(cx,cy)
            newy, newx = game_king.get_position()
            # print(posi[cy][cx].startswith("CANON"))
            damaged = False
            
            if(newx <= cy+2+5 and newy <= cx+3+5 and newx >= cy-5 and newy >= cx-5 and posi[cy][cx].startswith("CANON")):
                # print("Jay Bomdd")
                overr = game_king.reduce_health(10)
                damaged = True
                show = game_king.get_health()
                print(f"\033[31;0H"+Fore.WHITE + " ")
                print(f"\033[31;1H"+Fore.WHITE + " ")
                print(f"\033[31;2H"+Fore.WHITE + " ")
                print(f"\033[31;3H"+Fore.WHITE + " ")
                print(f"\033[31;4H"+Fore.WHITE + " ")
                print(f"\033[31;0H"+Fore.WHITE + f"{show}")
                if overr == 1:
                    os.system('clear')
                    print("DEFEAT")
                    print(f"{(game_king.building()/8)*100}"+"%")
                    break
            if damaged:
                continue
            for arch in archer_array:
                if arch.get_health() > 0:
                    newx, newy = arch.get_position()
                    newy = int(newy)
                    newx = int(newx)
                    # print(newx,cy,newy,cx)
                    # print(newx <= cy+2+5,newy <= cx+3+5,newx >= cy-5,newy >= cx-5)
                    if(newx <= cy+2+5 and newy <= cx+3+5 and newx >= cy-5 and newy >= cx-5 and posi[cy][cx].startswith("CANON")):
                        # print("Jay Bomdd")
                        oveeer = arch.reduce_health(10)
                        if oveeer == 1:
                            # print(newx,newy)
                            print(f"\033[{newx + 1};{newy + 1}H" +
                                  Fore.WHITE + " ")
                        break
                # else:
                #     newx, newy = arch.get_position()
                #     print(newx,newy)

        for wizz_coords in wizz_positions:
            cx, cy = wizz_coords[0], wizz_coords[1]
            
            # print(posi[cy][cx])
            newy, newx = game_king.get_position()
            # print(posi[cy][cx].startswith("CANON"))
            damaged = False
            # print(newy,newx)
            if(newx <= cy+2+5 and newy <= cx+3+5 and newx >= cy-5 and newy >= cx-5 and posi[cy][cx].startswith("WIZZ")):
                # print("Jay Bomdd")
                damaged = True
                overr = game_king.reduce_health(10)
                show = game_king.get_health()
                print(f"\033[31;0H"+Fore.WHITE + " ")
                print(f"\033[31;1H"+Fore.WHITE + " ")
                print(f"\033[31;2H"+Fore.WHITE + " ")
                print(f"\033[31;3H"+Fore.WHITE + " ")
                print(f"\033[31;4H"+Fore.WHITE + " ")
                print(f"\033[31;0H"+Fore.WHITE + f"{show}")
                if overr == 1:
                    os.system('clear')
                    print("DEFEAT")
                    print(f"{(game_king.building()/8)*100}"+"%")
                    break
            if damaged:
                continue
            for arch in archer_array:
                if arch.get_health() > 0:

                    # print(arch.get_health())
                    newx, newy = arch.get_position()
                    newy = int(newy)
                    newx = int(newx)
                    # print(newy,newx)
                    # print(newx,newy)
                    if(newx <= cy+2+5 and newy <= cx+3+5 and newx >= cy-5 and newy >= cx-5 and posi[cy][cx].startswith("WIZZ")):
                        # print("Jay Bomdd")
                        testt =arch.reduce_health(10)
                        if testt:
                            print(f"\033[{newx + 1};{newy + 1}H" +
                                  Fore.WHITE + " ")
                    

        if inp in ['w', 'a', 's', 'd']:
            game_king.saveDirection(inp)

        if(inp == None):
            pass
        elif inp == 'q':
            # os.system("clear")
            break
        elif inp == 'w':
            xking, yking = game_king.get_position()
            # print(game_bord.get_grid(yking-1,xking) == Back.BLACK + Fore.BLACK +" "
            # )

            if(ranges == 1):
                if(game_bord.get_grid(yking-1, xking) == Back.BLACK + Fore.BLACK + " "):
                    # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H" + " ")
                    print(f"\033[{yking+1-1};{xking+1}H" +
                          Fore.WHITE + game_king.design)
                    game_king.move_up(1)
            xking, yking = game_king.get_position()
            if(game_bord.get_grid(yking-1, xking) == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                print(f"\033[{yking+1};{xking+1}H" + " ")
                print(f"\033[{yking+1-1};{xking+1}H" +
                      Fore.WHITE + game_king.design)
                game_king.move_up(1)
            # else:
            #     print(game_bord.get_grid(yking,xking-1),Fore.WHITE + posi[yking-1][xking])
        elif inp == 'l':
            game_king.archer_queen_eagle_arrow(
                posi, hut_array, game_bord, canon_array, townhall_array, dbuilding, ranges, hut_positions, canon_positions,lev,initialize_bord3,initialize_bord2,Level2,Level3,keyyy,archer_array)
        elif inp == 'a':
            xking, yking = game_king.get_position()
            if(ranges == 1):
                if(game_bord.get_grid(yking, xking-1) == Back.BLACK + Fore.BLACK + " "):
                    # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H" + " ")
                    print(f"\033[{yking+1};{xking+1-1}H" +
                          Fore.WHITE + game_king.design)
                    game_king.move_left(1)
            xking, yking = game_king.get_position()
            if(game_bord.get_grid(yking, xking-1) == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                print(f"\033[{yking+1};{xking+1}H" + " ")
                print(f"\033[{yking+1};{xking+1-1}H" +
                      Fore.WHITE + game_king.design)
                game_king.move_left(1)

            # else:
            #     print(game_bord.get_grid(yking,xking-1),Fore.WHITE +posi[yking][xking-1])
        elif inp == 's':
            xking, yking = game_king.get_position()
            if(game_bord.get_grid(yking+1, xking) == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                print(f"\033[{yking+1};{xking+1}H" + " ")
                print(f"\033[{yking+1+1};{xking+1}H" +
                      Fore.WHITE + game_king.design)
                game_king.move_down(1)
            if(ranges == 1):
                xking, yking = game_king.get_position()
                if(game_bord.get_grid(yking+1, xking) == Back.BLACK + Fore.BLACK + " "):
                    # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H" + " ")
                    print(f"\033[{yking+1+1};{xking+1}H" +
                          Fore.WHITE + game_king.design)
                    game_king.move_down(1)
            # else:
            #     print(game_bord.get_grid(yking,xking-1),Fore.WHITE +posi[yking+1][xking])
        elif inp == 'd':
            xking, yking = game_king.get_position()
            if(game_bord.get_grid(yking, xking+1) == Back.BLACK + Fore.BLACK + " "):
                # print(game_bord.get_grid(yking,xking+1)==Back.BLACK + Fore.BLACK + " ")
                print(f"\033[{yking+1};{xking+1}H" + " ")
                print(f"\033[{yking+1};{xking+1+1}H" +
                      Fore.WHITE + game_king.design)
                game_king.move_right(1)
            if(ranges == 1):
                xking, yking = game_king.get_position()
                if(game_bord.get_grid(yking, xking+1) == Back.BLACK + Fore.BLACK + " "):
                    # print(game_bord.get_grid(yking,xking+1)==Back.BLACK + Fore.BLACK + " ")
                    print(f"\033[{yking+1};{xking+1}H" + " ")
                    print(f"\033[{yking+1};{xking+1+1}H" +
                          Fore.WHITE + game_king.design)
                    game_king.move_right(1)
            # else:
            #     print(game_bord.get_grid(yking,xking-1),Fore.WHITE +posi[yking][xking+1])
        elif inp == ' ':
            game_king.attack(posi, hut_array, game_bord,
                             canon_array, townhall_array, dbuilding, ranges, hut_positions, canon_positions, wizard_array, wizz_positions,lev,initialize_bord3,initialize_bord2,Level2,Level3,keyyy,archer_array)
            # print(hut_array[0].get_hitpoints())
        elif inp == 'e':
            # over = 1
            # os.system('clear')
            # print("DEFET")
            # print(game_king.building()/8)
            xx = game_king.get_health()
            if(xx + (xx/2) < 3000):
                val = xx + (xx/2)
            else:
                val = 3000
            print(f"\033[31;0H"+Fore.WHITE + " ")
            print(f"\033[31;1H"+Fore.WHITE + " ")
            print(f"\033[31;2H"+Fore.WHITE + " ")
            print(f"\033[31;3H"+Fore.WHITE + " ")
            print(f"\033[31;4H"+Fore.WHITE + " ")
            print(f"\033[31;0H"+Fore.WHITE + f"{val}")
            game_king.update_health(val)
        elif inp == 'r':
            ranges = 1
        # time.sleep(0.1)
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
    file.close()
