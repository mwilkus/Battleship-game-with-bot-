from os import system
from time import sleep
from data_convert import ships1,ships2,in_to_st

def print_map(arr, e=False):
    print("   ", end="")
    for i in range(0,10):
        print(in_to_st[i+1],end=" ")
    print("")
    for num,i in enumerate(arr):
        if num!=9: print(num+1, end="  ")
        else: print(num+1, end=" ")
        for j in i:
            if not e:
                if j.ship==False and j.shot==False: print(".", end=" ")
                elif j.ship==True and j.shot==True and j.drowned==False: print("X", end=" ")
                elif j.ship==True and j.shot==True and j.drowned==True: print("@", end=" ")
                elif j.ship==True and j.shot==False: print("#", end=" ")
                elif j.ship==False and j.shot==True: print("M", end=" ")
            else:
                if j.ship==True and j.shot==True and j.drowned==False: print("X", end=" ")
                elif j.ship==True and j.shot==True and j.drowned==True: print("@", end=" ")
                elif j.ship==False and j.shot==True: print("M", end=" ")
                else: print(".", end=" ")
        print("")


def print_s():
    count_of_ships={1:0,2:0,3:0,4:0,5:0}
    count_of_ships_e={1:0,2:0,3:0,4:0,5:0}
    for ship in ships1:
        if not ship.destroy: count_of_ships[len(ship)]+=1
    for ship in ships2:
        if not ship.destroy: count_of_ships_e[len(ship)]+=1
    is_win(count_of_ships, count_of_ships_e)
    print(f"You: #-{count_of_ships[1]},  ##-{count_of_ships[2]},  ###-{count_of_ships[3]},  ####-{count_of_ships[4]},  #####-{count_of_ships[5]}")
    print(f"Enemy: #-{count_of_ships_e[1]},  ##-{count_of_ships_e[2]},  ###-{count_of_ships_e[3]},  ####-{count_of_ships_e[4]},  #####-{count_of_ships_e[5]}")

def is_win(count_of_ships, count_of_ships_e):
    you=0;enemy=0
    for i in count_of_ships.values(): you+=i
    for i in count_of_ships_e.values(): enemy+=i
    if enemy==0:
        system("clear")
        print("YOU WIN!")
        sleep(3)
        exit(0)
    elif you==0:
        system("clear")
        print("YOU LOSE!")
        sleep(3)
        exit(0)