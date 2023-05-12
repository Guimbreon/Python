"""
Counting in files

"""
import re

FILE = "/home/guimbreon/Desktop/GIT_TESTS/Python/Pdf_Counter/LICENSE"

with open(f"{FILE}","r",encoding="utf-8") as pdf:
    EVERYTHING = [] 
    for item in pdf:
        EVERYTHING.append(item.replace("\n",""))

def Total_Words(EVERYTHING):
    """
    Funtion to count the amout of words in the file.
    Output: Almost Perfect. WHY:
        Have fixed that it counts words separated by / but now it gives-me more words than it was supossed to
    """
    Total_Word_Count = 0
    for line in EVERYTHING:
        print(line)
        if line != "":
            for word in line.split(" "):
                if "/" in word:
                    for item in word.split("/"):
                        if item != "" and item != " ":
                            Total_Word_Count += 1
                else:
                    if word != "" or " " in word:
                        Total_Word_Count += 1
    return Total_Word_Count


def Line_Counter(EVERYTHING):
    """
    Funtion to count the amount of lines there are in the file.
    Output: Perfect
    """
    Line_Count = 0
    for line in EVERYTHING:
        Line_Count += 1
    return Line_Count

def Character_Counter(EVERYTHING):
    """
    Count the Characters.
    Output: Perfect
    """
    Character_Count = 0
    for line in EVERYTHING:
        print(line)
        for thing in line:
            print(thing)
            Character_Count += 1
    return Character_Count

print(EVERYTHING)
choice = input("""
What do you want to do with that file?
1- Count the total Words
2- Count the Lines
3- Count all the characters
4- Count a specific Word.
>>
""")
if choice == "1":
    Word_Count = Total_Words(EVERYTHING)
    print(f"\nThe file has a total of {Word_Count} words.")

elif choice == "2":
    Line_Count = Line_Counter(EVERYTHING)
    print(f"\nThe file has a total of {Line_Count} lines.")
elif choice == "3":
    Character_Count = Character_Counter(EVERYTHING)
    print(Character_Count)
elif choice == "4":
    print("Will be added soon!")
else:
    print("\nU didn't give me a viable option!")

