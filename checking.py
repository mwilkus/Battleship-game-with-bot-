from time import sleep
from os import system
from data_convert import *

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

def drown(row,col,e=False):
    if not e:
        ships=ships2
        mapx=map2
    else:
        ships=ships1
        mapx=map1
    for ship in ships:
        if ship.destroy==False:
            row1,col1=ship.start
            row2,col2=ship.end
            if row1==row2:
                if row==row1 and col in range(min(col1,col2),max(col1,col2)+1):
                    dest=True
                    for i in range(min(col1,col2),max(col1,col2)+1):
                        if mapx[row][i].shot==False: dest=False
                    if dest:
                        ship.destroy=True
                        for i in range(min(col1, col2), max(col1, col2) + 1):
                            mapx[row][i].drowned=True
                            if e==True: targets.remove((row,i))
                        return True
            elif col1==col2:
                if col==col1 and row in range(min(row1,row2),max(row1,row2)+1):
                    dest=True
                    for i in range(min(row1,row2),max(row1,row2)+1):
                        if mapx[i][col].shot==False: dest=False
                    if dest:
                        for i in range(min(row1, row2), max(row1, row2) + 1):
                            mapx[i][col].drowned=True
                            if e==True: targets.remove((i, col))
                        ship.destroy=True
                        return True
    return False