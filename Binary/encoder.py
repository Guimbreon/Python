"""
Binary translator in python
"""
#Processing the transalation library:

FILE = "/home/guimbreon/Desktop/Git_organazier/Tests/Binary_translator/Keys"
data={}
with open(FILE, "r", encoding="utf8") as file:
    data={}
    for line in file:
        line=line.split(":")
        data[line[0]]=line[1].replace("\n","")

#Getting the input from the user

QUOTE=input("""
WELCOME TO THE BINARY TRANSLATOR 0.5!!!

DON'T FORGET U CAN ONLY USE LETTERS HERE!\n>>> """)

#Encoding

NEW_QUOTE=""
for letter in QUOTE:
    NEW_QUOTE+=data[letter]

print(NEW_QUOTE)
