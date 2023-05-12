programa = """
This program reads the file and then:

    1- Count the total Words
    2- Count the Lines
    3- Count all the characters
    4- Count a specific Word.
"""

#argparser part of the program
import sys

if len(sys.argv) != 2:
    print("""You either provided extra files or didn't have enought files.
    You have to run the program like:
    Python3 Txt_Counter.py FILE_NAME""")
    quit()

with open(f"{sys.argv[1]}","r",encoding="utf-8") as pdf:
    EVERYTHING = [] 
    for item in pdf:
        EVERYTHING.append(item.replace("\n",""))

def Total_Words(text):
    """
    Funtion to count the amout of words in the file.
    Output: Almost Perfect. WHY:
        Have fixed that it counts words separated by / but now it gives-me more words than it was supossed to
    """
    Total_Word_Count = 0
    for line in text:
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


def Line_Counter(text):
    """
    Funtion to count the amount of lines there are in the file.
    Output: Perfect
    """
    Line_Count = 0
    for line in text:
        Line_Count += 1
    return Line_Count

def Character_Counter(text):
    """
    Count the Characters.
    Output: Perfect
    """
    Character_Count = 0
    for line in text:
        for thing in line:
            Character_Count += 1
    return Character_Count

def Specific_word(text,which):
    Specific_word_Count = 0

    for line in text:
        if line != "":
            for word in line.split(" "):
                if "/" in word:
                    for item in word.split("/"):
                        if item != "" and item != " ":
                            Specific_word_Count +=1
                else:
                    if word != "" or " " in word:
                        if word == which:
                            Specific_word_Count +=1
    return Specific_word_Count

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
    which = input("Which word do you want to analyze?\n>>")
    Specific_word_Count = Specific_word(EVERYTHING,which)
    print(f"The amount of the word '{which}' in this file are {Specific_word_Count}")
else:
    print("\nU didn't give me a viable option!")

