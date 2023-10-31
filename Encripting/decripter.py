import sys

def info(encripted,file):
    with open(file, "r") as file:
        for line in file:
            if line.startswith(">"):
                letters.append(line.replace("\n","").replace(">",""))
            else:
                subs.append(line.replace("\n",""))
    i=0
    for thing in letters:
        letter_sub[subs[i]]=thing
        i+=1
    return subs,letter_sub
#translation
def translation(encripted,subs,letter_sub):
    divided=[]
    every_letter=[]
    part=""
    parts=[]
    #this part does the separation by every even slot
    for letter in encripted:
        part+=letter
        if len(part)==len(encripted)/2 and len(encripted)%2==0:
            parts.append(part)
            part=""
        elif len(part)==(len(encripted)//2)+1 and len(encripted)%2!=0:
            parts.append(part)
            part=""
        elif len(part)==(len(encripted)//2) and len(parts)!=0:
            parts.append(part)
    
    part=""
    parts=[]
    for letter in encripted:
        part+=letter
        if len(part)==len(encripted)/2 and len(encripted)%2==0:
            parts.append(part)
            part=""
        elif len(part)==(len(encripted)//2)+1 and len(encripted)%2!=0:
            parts.append(part)
            part=""
        elif len(part)==(len(encripted)//2) and len(parts)!=0:
            parts.append(f"{part}~")
    first_part,second_part=parts[0],parts[1]
    i=0
    new_encripted=""
    for letter in first_part:
        new_encripted+=letter+second_part[i]
        i+=1
    encripted=new_encripted.replace("~","")
    #the normal rest
    while encripted!="":
        divided.append(encripted[:5])
        encripted=encripted[5:]
    for item in subs:
        if item not in divided:
            print("The encripted message CANNOT be translated by the doc_key!\n")
            quit()
    quote=""
    for item in divided:
        quote+=letter_sub[f"{item}"]
    return quote