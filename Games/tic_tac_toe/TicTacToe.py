import random
input("""\n
Welcome to TIK TAK TOE!
After playing u'll be asked which simbol each player wants to play has...

The model of the game is the follwoing:
1|2|3
4|5|6
7|8|9

U'll have to say the number corresponding to the spot u want to play in.

Press any key to continue...""")
key=[""]*3
key[1]=input("\nPLAYER 1:\nWhich simbol do you u want to play has?\n>>")
key[2]=input("\nPLAYER 2:\nWhich simbol do you u want to play has?\n>>")
which=random.randint(1,2)

print(f"\nThe machine will choose who plays first randomly!\nThe PLAYER {which} plays first!")

end=0

error=0

def check(i):
    global which,end
    error = 0
    if play[1] == play[2] and play[2] == play[3]:
        end=1
    elif play[4] == play[5] and play[5] == play[6]:
        end=1
    elif play[7] == play[8] and play[8] == play[9]:
        end=1
    elif play[1] == play[4] and play[4] == play[7]:
        end=1
    elif play[2] == play[5] and play[5] == play[8]:
        end=1
    elif play[3] == play[6] and play[6] == play[9]:
        end=1
    elif play[1] == play[5] and play[5] == play[9]:
        end=1
    elif play[3] == play[5] and play[5] == play[7]:
        end = 1
    if error != 1:
        if which == 1 and end == 0:
            which += 1
        elif which == 2 and end == 0:
            which -= 1
    else:
        which = which

    count=0
    
    for item in play:
        if item not in range(0,9):
            count+=1
    if count == 9:
        end=1


play = ["0","1","2","3","4","5","6","7","8","9"]

while end != 1:
    i = input(f"""\nWhere do you wanna play PLAYER {which}?\n
                {play[1]}|{play[2]}|{play[3]}
                {play[4]}|{play[5]}|{play[6]}
                {play[7]}|{play[8]}|{play[9]}
    >>""")
    if i not in play:
        print("\nThe digit you entered isn't a posible spot position!")
        error = 2
    if error !=2:
        i = int(i)
        if play[i] == key[1] or play[i] == key[2]:
            input("\nU can't choose that spot!\n")
            error = 1
        else:
            play[i] = key[which]
            error = 0
        check(i)

if end == 1:
    print(f"""\n
    THE END!
                    1|2|3\t\t{play[1]}|{play[2]}|{play[3]}
                    4|5|6\t\t{play[4]}|{play[5]}|{play[6]}
                    7|8|9\t\t{play[7]}|{play[8]}|{play[9]}
    PLAYER {which} u won!
        """)

else:
    print(f"""\n
    THE END!
                    1|2|3\t\t{play[1]}|{play[2]}|{play[3]}
                    4|5|6\t\t{play[4]}|{play[5]}|{play[6]}
                    7|8|9\t\t{play[7]}|{play[8]}|{play[9]}
        It was a draw!
        """)