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
        data[line[1].replace("\n","")]=line[0]

#Getting the input from the user

QUOTE=input("""
WELCOME TO THE BINARY TRANSLATOR 0.5!!!

WRITE WHAT YOU WANT TO TRANSLATE\n>>> """)

#Translator
SEP=""
SEP_QUOTE=[]
for number in QUOTE:
    SEP+=number
    if len(SEP)==8:
        SEP_QUOTE.append(SEP)
        SEP=""
TRANSLATED=""

for item in SEP_QUOTE:
    TRANSLATED+=data[item]
print(TRANSLATED)
