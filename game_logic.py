from print_functions import *
from data_convert import *
from checking import drown
from json import loads

def turn():
    print_map(map1)
    print("\n")
    print_s()
    print("\n")
    print_map(map2, e=True)
    while True:
        try:
            print("Where you want to shot?")
            inp=input()
            if input_convert(inp)==False: raise Exception()
            else: col,row=input_convert(inp)
            col=st_to_in[col]
            if map2[row-1][col-1].shot==True: raise Exception()
            map2[row-1][col-1].shot=True
            if map2[row-1][col-1].ship==True:
                print("Hit!!!")
                if drown(row-1,col-1)==False: print("Don,t drown")
                else: print("Drown")
            else: print("Miss!!")
            sleep(1)
            system("clear")
            break
        except:
            print("Bad input")
            sleep(1)

def e_turn():
    if targets==[]:
        he_map=[]
        for i in range(0,10):
            row=[]
            for j in range(0,10):
                row.append(0)
            he_map.append(row)
        with open("settings.json") as f: data = loads(f.read())
        for i in range(0,5):
            for j in range(data["ships"][str(i+1)]["count"],0,-1):

                for row in range(0,10):
                    for col in range(0,10):
                        if col+i+1<=10:
                            stop=False
                            for po in range(col,col+i+1):
                                if map1[row][po].shot==True:
                                    stop=True
                            if not stop:
                                for po in range(col,col+i+1):
                                    he_map[row][po]+=1

                for col in range(0,10):
                    for row in range(0,10):
                        if row+i+1<=10:
                            stop=False
                            for po in range(row,row+i+1):
                                if map1[po][col].shot==True:
                                    stop=True
                            if not stop:
                                for po in range(row,row+i+1):
                                    he_map[po][col]+=1

        dmax=0;r_max=0;c_max=0
        for num1,line in enumerate(he_map):
            for num2,pol in enumerate(line):
                if pol>dmax:
                    dmax=pol
                    r_max=num1
                    c_max=num2

        shot(r_max,c_max)


    else:
        row,col=targets[-1]
        while True:
            urdl_points=[0,0,0,0]
            if row+1>=10: urdl_points[0]=-10000
            if row-1<0: urdl_points[2]=-10000
            if col+1>=10: urdl_points[1]=-10000
            if col-1<0: urdl_points[3]=-10000
            if urdl_points[0]!=-10000:
                if row-1>=0:
                    if map1[row-1][col].shot==True and map1[row-1][col].drowned==False and map1[row-1][col].ship==True: urdl_points[0]+=1
                if map1[row+1][col].shot==True: urdl_points[0]=-10000
            if urdl_points[2]!=-10000:
                if row+1<10:
                    if map1[row+1][col].shot==True and map1[row+1][col].drowned==False and map1[row+1][col].ship==True: urdl_points[2]+=1
                if map1[row-1][col].shot==True: urdl_points[2] = -10000
            if urdl_points[1]!=-10000:
                if col-1>=0:
                    if map1[row][col-1].shot==True and map1[row][col-1].drowned==False and map1[row][col-1].ship==True: urdl_points[1]+=1
                if map1[row][col+1].shot==True: urdl_points[1] = -10000
            if urdl_points[3]!=-10000:
                if col+1<10:
                    if map1[row][col+1].shot==True and map1[row][col+1].drowned==False and map1[row][col+1].ship==True: urdl_points[3]+=1
                if map1[row][col-1].shot==True: urdl_points[3] = -10000
            for num,targ in enumerate(urdl_points):
                if targ==max(urdl_points) and max(urdl_points)!=-10000:
                    if num==0:
                        shot(row+1,col)
                        return 0
                    elif num==1:
                        shot(row,col+1)
                        return 0
                    elif num==2:
                        shot(row-1,col)
                        return 0
                    elif num==3:
                        shot(row,col-1)
                        return 0
                elif max(urdl_points)==-10000:
                    row,col=targets[0]
                    break


def shot(row,col):
    map1[row][col].shot=True
    if map1[row][col].ship==True:
        print("Enemy Hit!!!")
        targets.append((row,col))
        if drown(row, col, e=True) == False: print("Don,t drown")
        else: print("Drown")
    else:
        print("Enemy Miss!!")