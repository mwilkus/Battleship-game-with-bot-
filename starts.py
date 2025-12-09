from os import system
from random import randint
from time import sleep
from json import loads
from print_functions import print_map
from data_convert import *
from data_classes import Ship

def start(inp1="",inp2="",e=False,z=0):
    with open("settings.json") as f: data=loads(f.read())
    for i in range(0,5):
        for j in range(data["ships"][str(i+1)]["count"],0,-1):
            while (True):
                try:
                    if not e:
                        system("clear")
                        print(data["ships"][str(i+1)]["count"])
                        print_map(map1)
                        print(f"Choose place of your l={i+1} ship ({j} left)")
                        print("Choose start id")
                        inp1=input()
                        if i+1>1:
                            print(f"Choose end id")
                            inp2=input()
                        else:
                            inp2=inp1
                    if input_convert(inp1)==False or input_convert(inp2)==False: raise Exception()
                    else:
                        col1,row1=input_convert(inp1)
                        col1=st_to_in[col1]
                        col2,row2=input_convert(inp2)
                        col2=st_to_in[col2]
                        if not e:
                            if not ((row1==row2 and abs(col1-col2)==i) or (col1==col2 and abs(row1-row2)==i)): raise Exception()
                        else:
                            if not ((row1==row2 and abs(col1-col2)==z) or (col1==col2 and abs(row1-row2)==z)): raise Exception()

                        if not e:
                            if row1==row2:
                                for m in range(min(col1,col2),max(col1,col2)+1):
                                    if map1[row1-1][m-1].ship==True: raise Exception()
                            else:
                                for m in range(min(row1,row2),max(row1,row2)+1):
                                    if map1[m-1][col1-1].ship==True: raise Exception()

                            ######################################################
                            if row1==row2:
                                for m in range(min(col1,col2),max(col1,col2)+1):
                                    map1[row1-1][m-1].ship=True
                            else:
                                for m in range(min(row1,row2),max(row1,row2)+1):
                                    map1[m-1][col1-1].ship=True
                            ships1.append(Ship((row1-1,col1-1),(row2-1,col2-1),False))
                            ######################################################
                        else:
                            if row1 == row2:
                                for m in range(min(col1,col2),max(col1,col2)+1):
                                    if map2[row1-1][m-1].ship==True: raise Exception()
                            else:
                                for m in range(min(row1,row2),max(row1,row2)+1):
                                    if map2[m-1][col1-1].ship==True: raise Exception()

                            ######################################################
                            if row1 == row2:
                                for m in range(min(col1,col2),max(col1,col2)+1):
                                    map2[row1-1][m-1].ship=True
                            else:
                                for m in range(min(row1,row2),max(row1,row2)+1):
                                    map2[m-1][col1-1].ship=True
                            ships2.append(Ship((row1-1,col1-1),(row2-1,col2-1),False))
                            ######################################################
                        if not e: break
                        else: return True
                except:
                    if not e:
                        print("Bad input")
                        sleep(1)
                    else:
                        return False
    system("clear")
    print("Starting....")
    sleep(1)
    system("clear")



def e_start():
    with open("settings.json") as f: data = loads(f.read())
    for i in range(0,5):
        for j in range(data["ships"][str(i+1)]["count"],0,-1):
            while (True):
                row1=randint(1, 10)
                col1=randint(1, 10)
                h_or_v=randint(1,2)
                if h_or_v==1:
                    row2=min(row1+i,10)
                    col2=col1
                else:
                    col2=min(col1+i,10)
                    row2=row1
                res1=in_to_st[col1]+str(row1)
                res2=in_to_st[col2]+str(row2)
                if start(inp1=res1,inp2=res2,e=True,z=i) == True: break