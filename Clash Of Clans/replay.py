import colorama
from colorama import Fore, Back, Style
import termios
import subprocess as sp
import time
import tty
import sys
import os
import signal
from src.bord import *
from src.func import *
from src.input import *
from src.config import *
from src.king import *

# colorama.init() 
z = int(sys.argv[1])
ranges = 0
file = open(f'replays/{z}.txt', "r")
lines = file.readlines()
count = 0
if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    os.system("clear")
    inputs=Get()
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    initialize_bord1()
    while(1):
       
        inp = lines[count][0]
        count += 1

        newy,newx=game_king.get_position()
        # =game_king.get_position()
        if(newx <= 21 and newy <=34 and newx >= 8  and newy >= 21 and posi[13][26]=="CANON1"):
            show=game_king.get_health()
            # print(show)
            overr=game_king.reduce_health(canon_array[0].get_damage())
            print(f"\033[31;0H"+Fore.WHITE + " ")
            print(f"\033[31;1H"+Fore.WHITE + " ")
            print(f"\033[31;2H"+Fore.WHITE + " ")
            print(f"\033[31;3H"+Fore.WHITE + " ")
            print(f"\033[31;4H"+Fore.WHITE + " ")
            print(f"\033[31;0H"+Fore.WHITE + f"{show}")
            if overr==1:
                os.system('clear')
                print("DEFET")
                print(f"{(game_king.building()/8)*100}"+"%")
                break
        elif(newx <= 21 and newy <=67 and newx >= 8  and newy >= 54 and posi[13][59]=="CANON2"):
            show=game_king.get_health()
            # print(show)
            overr=game_king.reduce_health(canon_array[0].get_damage())
            print(f"\033[31;0H"+Fore.WHITE + " ")
            print(f"\033[31;1H"+Fore.WHITE + " ")
            print(f"\033[31;2H"+Fore.WHITE + " ")
            print(f"\033[31;3H"+Fore.WHITE + " ")
            print(f"\033[31;4H"+Fore.WHITE + " ")
            print(f"\033[31;0H"+Fore.WHITE + f"{show}")
            if overr==1:
                os.system('clear')
                print("DEFET")
                print(f"{(game_king.building()/8)*100}"+"%")
                break
        

        if(inp=="-"):
            pass
        elif inp=='q':
            os.system("clear")
            break
        elif inp=='w':
            xking,yking = game_king.get_position()
            # print(game_bord.get_grid(yking-1,xking) == Back.BLACK + Fore.BLACK +" " )
            if(ranges==1):
                if(game_bord.get_grid(yking-1,xking)  == Back.BLACK + Fore.BLACK + " "):
                    # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H"+ " ")
                    print(f"\033[{yking+1-1};{xking+1}H"+Fore.WHITE + "K")
                    game_king.move_up(1)
            xking,yking = game_king.get_position()
            if(game_bord.get_grid(yking-1,xking)  == Back.BLACK + Fore.BLACK + " "):
                    # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H"+ " ")
                    print(f"\033[{yking+1-1};{xking+1}H"+Fore.WHITE + "K")
                    game_king.move_up(1)
           

        elif inp=='a':
            xking,yking = game_king.get_position()
            if(ranges==1):
                if(game_bord.get_grid(yking,xking-1)  == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H"+ " ")
                    print(f"\033[{yking+1};{xking+1-1}H"+ Fore.WHITE +"K")
                    game_king.move_left(1)
            xking,yking = game_king.get_position()
            if(game_bord.get_grid(yking,xking-1)  == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                print(f"\033[{yking+1};{xking+1}H"+ " ")
                print(f"\033[{yking+1};{xking+1-1}H"+ Fore.WHITE +"K")
                game_king.move_left(1)
                
        elif inp=='s':
            xking,yking = game_king.get_position()
            if(game_bord.get_grid(yking+1,xking)  == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                print(f"\033[{yking+1};{xking+1}H"+ " ")
                print(f"\033[{yking+1+1};{xking+1}H"+ Fore.WHITE +"K")
                game_king.move_down(1)
            if(ranges==1):
                xking,yking = game_king.get_position()
                if(game_bord.get_grid(yking+1,xking)  == Back.BLACK + Fore.BLACK + " "):
                # print(xking,yking)
                    print(f"\033[{yking+1};{xking+1}H"+ " ")
                    print(f"\033[{yking+1+1};{xking+1}H"+ Fore.WHITE +"K")
                    game_king.move_down(1)
        elif inp=='d':
            xking,yking = game_king.get_position()
            if(game_bord.get_grid(yking,xking+1)  == Back.BLACK + Fore.BLACK + " "):
                # print(game_bord.get_grid(yking,xking+1)==Back.BLACK + Fore.BLACK + " ")
                print(f"\033[{yking+1};{xking+1}H"+ " ")
                print(f"\033[{yking+1};{xking+1+1}H"+ Fore.WHITE +"K")
                game_king.move_right(1)
            if(ranges==1):
                xking,yking = game_king.get_position()
                if(game_bord.get_grid(yking,xking+1)  == Back.BLACK + Fore.BLACK + " "):
                # print(game_bord.get_grid(yking,xking+1)==Back.BLACK + Fore.BLACK + " ")
                    print(f"\033[{yking+1};{xking+1}H"+ " ")
                    print(f"\033[{yking+1};{xking+1+1}H"+ Fore.WHITE +"K")
                    game_king.move_right(1)
        elif inp==' ':
            game_king.attack(posi,hut_array,game_bord,canon_array,townhall_array,dbuilding,ranges)
            # print(hut_array[0].get_hitpoints())
        elif inp=='e':
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
        elif inp=='r':
            ranges = 1
        time.sleep(0.1)
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()
    