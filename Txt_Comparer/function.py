
def Word_Counting(FILE):


    with open(FILE,"r",encoding="utf-8") as text:
        Quotes = []
        for thing in text:
            thing = thing.replace("\n","")
            if "" != thing:
                Quotes.append(thing)


    Word = []

    for quote in Quotes:
        for thing in quote.split(" "):
            if thing != "":
                Word.append(thing)
            
    Count = {}

    for item in Word:
        if item not in Count:
            Count[item] = 1
        else:
            Count[item] += 1

    return Count




Sum_words_1 = Word_Counting(FILE=input("What is the main file you want to analyze=\n>>").replace("'",""))

Sum_words_2 = Word_Counting(FILE=input("What is the second file you want to analyze?\n>>").replace("'",""))


same = 0

different = 0

for key in Sum_words_1:
    if key in Sum_words_2.keys():
        if Sum_words_1[key]-Sum_words_2[key] == 0:
            same += Sum_words_1[key]
        else:
            different += abs(Sum_words_1[key]-Sum_words_2[key])
            same += Sum_words_1[key] - abs(Sum_words_1[key]-Sum_words_2[key])
    else:
        different += Sum_words_1[key]

percentage = (different/same)*100

print(different,same)
print(f"""The amount of words that are in the same amount is {same}.
The amount of words that are in different amount is {different}.
Which leads to {round(percentage,2)}%""")