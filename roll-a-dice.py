import random

def randint(start, end):
    response = "y"
    while response=="y":
        no = int(random.randint(start, end))
        if (no==1):
            print("[---]")
            print("[   ]")
            print("[ 0 ]")
            print("[   ]")
            print("[---]")
        elif (no==2):
            print("[---]")
            print("[0  ]")
            print("[   ]")
            print("[  0]")
            print("[---]")
        elif (no==3):
            print("[---]")
            print("[0  ]")
            print("[ 0 ]")
            print("[  0]")
            print("[---]")
        elif (no==4):
            print("[---]")
            print("[0 0]")
            print("[   ]")
            print("[0 0]")
            print("[---]")
        elif (no==5):
            print("[---]")
            print("[0 0]")
            print("[ 0 ]")
            print("[0 0]")
            print("[---]")
        elif (no==6):     
            print("[---]")
            print("[0 0]")
            print("[0 0]")
            print("[0 0]")
            print("[---]")
        response = input("Press y to roll again and n to exit:  ")

randint(1,6)
