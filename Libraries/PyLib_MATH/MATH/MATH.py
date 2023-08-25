"""
First works on trying to create libraries
"""

def Sum(Num1,Num2):
    """
    Sum of the numbers the user gave!
    """
    return Num1 + Num2

def Sub(Num1,Num2):
    """
    Subtraction of the numbers the user gave.
    """
    return Num1-Num2

def Mult(Num1,Num2):
    """
    Multiplication of the numbers the user gave.
    """
    return Num1*Num2

def Div(Num1,Num2):
    """
    Divition of the numbers the user gave.
    """
    return Num1/Num2

def Eleva(Num1,Num2):
    """
    Raises the first number by the second!
    """
    return Num1**Num2

def Fibonacci(number):
    """to get fibonacci sequence"""
    num1 = 1
    num2 = 1
    num3 = 0
    all_numbers = [1,]
    for i in range(number-1):
        num3 = num1 + num2
        all_numbers.append(num2)
        num1=num2
        num2=num3
    return all_numbers


def Trend(list_number):
    """
    To get the most common number
    """
    Count_Number = {}
    for number in list_number:
        if number not in Count_Number.keys():
            Count_Number[number] = 1
        else:
            Count_Number[number] += 1

    sum = -999*999*999*999*999*999*999
    trend = -999*999*999*999*999*999*999

    for item in Count_Number.keys():
        if Count_Number[item] > trend:
            sum = Count_Number[item]
            trend = item
    print(Count_Number)
    return trend

def Max(list_number):
    """
    Returns the biggest number in the list
    """
    max = -999*999*999*999*999*999*999
    for item in list_number:
        if item > min:
            max = item
    return max

def Min(list_number):
    """
    Returns the smallest number in the list
    """
    min = 999*999*999*999*999*999*999
    for item in list_number:
        if item < min:
            min = item
    return min

def Mean(list_number):
    """
    Returns the mean of the list
    """
    mean = 0
    for item in list_number:
        mean += item
    
    mean = mean/len(list_number)

    return mean

def Fact(number):
    """
    Returns the factorial of the number the user gives
    """
    factorial = 1
    for i in range(1,number+1):
        factorial*=i
    return factorial

def sqrt(num):
    """
    Returns the square_root of the number using the Newton-Paphson metod
    """
    if num < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo.")
    elif num == 0:
        return 0
    else:
        x = num
        # Iterates the difference between x**2 that is smaller than 0.0001
        while abs(x * x - num) > 0.0001:
            # Calculate in Aproximation
            x = (x + num / x) / 2

        return round(x,5)