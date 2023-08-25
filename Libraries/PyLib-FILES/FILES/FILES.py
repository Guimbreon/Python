def Read(PATH):
    """
    Helps users read files!!!
    """
    Quotes = []
    with open(PATH, "r") as file:
        for item in file:
            Quotes.append(item)
    return Quotes

def Write(PATH,Writting):
    """
    Helps users write in files
    """
    with open(PATH, "w") as file:
        for item in Writting:
          file.write(item)