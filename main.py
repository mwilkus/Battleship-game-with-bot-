from json import dumps
from data_classes import Pole
from starts import *
from game_logic import e_turn,turn


def settings():
    with open("settings.json") as f:
        data=loads(f.read())
    while True:
        system("clear")
        print("Chose count of ships")
        print(f"5. l=5 ships {data["ships"]["5"]["count"]} (max={data["ships"]["5"]["max"]})")
        print(f"4. l=4 ships {data["ships"]["4"]["count"]} (max={data["ships"]["4"]["max"]})")
        print(f"3. l=3 ships {data["ships"]["3"]["count"]} (max={data["ships"]["3"]["max"]})")
        print(f"2. l=2 ships {data["ships"]["2"]["count"]} (max={data["ships"]["2"]["max"]})")
        print(f"1. l=1 ships {data["ships"]["1"]["count"]} (max={data["ships"]["1"]["max"]})")
        print("q - quit")
        while True:
            x=input("Choose type of ship: ")
            if x=="q":
                system("clear")
                return 0
            try:
                if (int(x) in range(1,6)):
                    pass
                else: raise Exception()
            except Exception:
                print("Invalid input")
                continue
            y=input("Count of ships: ")
            try:
                if int(y)<=data["ships"][x]["max"] and int(y)>=0:
                    data["ships"][x]["count"]=int(y)
                    with open("settings.json","w") as f:
                        f.write(dumps(data, indent=4))
                    break
                else: raise Exception()
            except Exception:
                print("Invalid input")
                continue


def menu():
    while True:
        system("clear")
        print("Welcome in the game!")
        print("1. Start")
        print("2. Settings")
        print("q. Exit")
        while True:
            x=input()
            if x=="1":
                return 0
            elif x=="2":
                settings()
                break
            elif x=="q":
                exit()
            else:
                print("Invalid input")
                continue


#################################################################################################
if __name__=="__main__":
    for i in range(10):
        row1 = []
        row2 = []
        row3 = []
        for j in range(10):
            row1.append(Pole(i + 1, j + 1, False, False, False))
            row2.append(Pole(i + 1, j + 1, False, False, False))
            row3.append(Pole(i + 1, j + 1, False, False, False))
        map1.append(row1)
        map2.append(row2)
    menu()
    start()
    e_start()
    while True:
        e_turn()
        turn()


