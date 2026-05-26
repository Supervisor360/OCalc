import math
import random
import os

ver = "v1.0"

#Misc Functions
def prompt(): #Help
    print('''
    NOTE: Commands are not Case Sensitive.
    
    Available Commands:
    HELP - list available commands
    QUIT - Quit/Exit Program
    ABOUT - Information about the program
    CLEAR - clear screen
    MLOAD - Load from Memory
    MSAVE - Save to Memory
    MUL - Multiply
    DIV - Divide
    SUB - Subtract
    ADD - Addition
    ROOT - Root Extraction
    EXPO - Exponentiation
    PERC - Percentage
    AVRG - Average Number
    MEDN - Median Number
    RAND - Random Number
    TRIG - Trigonometry
    PYTH - Pythagorian Theorem
    AREA - Find Area
    PERI - Perimeter
    VOLU - Find Volume
    SURA - Find Surface Area
    ''')
    return

result = 0
m1 = 0

def close(): #Quit Program
    print("Exiting Program")
    exit()

def about(): #About the program
    global ver
    print(f"OCalc {ver} by Regnbuebörk (Started 21/5/2026)")
    print("This is an Open Source multi-function & multi-purpose calculator program written entirely by one person in Python (NO AI) using PyCharm. It was mainly done to test my abilities in Python, as well as the fact I do not like most calculator programs and prefer the CLI interface. This program is intended to be published on pip and such for public usage and evaluation. Do note the program is very early in development and I am a beginner in Python. Thus, several functions may be incorrect and bugs may populate the code, despite my attempts to repair them. If you encounter any issues, please note them in the github and give me time to review, fix, and update the code and github repository with newer versions.")

def clear():
    # noinspection PyDeprecation
    os.system('cls' if os.name == 'nt' else 'clear')
    print("REGNBUEBÖRK Software 2026 - OCalc")
    print('Type "HELP" for a list of commands')

#Actual Calculation
def mul(): #Multiplication
    global result
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 * num2
    print(f'The result is {result}')

def div(): #Division
    global result
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 / num2
    print(f'The result is {result}')
    return

def sub(): #Subtraction
    global result
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 - num2
    print(f'The result is {result}')
    return

def add(): #Addition
    global result
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    result = num1 + num2
    print(f'The result is {result}')
    return

def root(): #Root Extraction
    global result
    num1 = int(input('Enter number to root: '))
    num2 = int(input('How many times should this number be rooted: '))
    result = num1 ** (1/num2)
    print(f'The result is {result}')
    return

def expo(): #Exponentiation
    global result
    num1 = int(input('Enter number to raise by a power: '))
    num2 = int(input('How many times should this number be raised:'))
    result = num1 ** num2
    print(f'The result is {result}')
    return

def perc(): #Percentage
    global result
    num1 = int(input('Total Number: '))
    num2 = int(input(f'Percentage of {num1} to find: '))
    result = (num2/100) * num1
    print(f'{num2}% is {result} of {num1}')
    return

def trig(): #Trigonometry
    global result
    num1 = int(input('Angle Degree: '))
    num2 = math.radians(num1)
    while True:
     sct = input("Sin, Cos, or Tan: ").upper()
     if sct == "SIN":
         result = (math.sin(num2))
         print(result)
         break
     if sct == "COS":
         result = (math.cos(num2))
         print(result)
         break
     if sct == "TAN":
         result = (math.tan(num2))
         print(result)
         break
     if sct == "":
         continue
     else:
         print("Please input Sin, Cos, or Tan")
         continue

def pyth(): #Pythagorean Theorem
    while True:
        global result
        q = input("Are you solving HYP(otenuse) or SIDE?: ").upper()
        if q == "HYP":
            num1 = int(input("Enter first side: "))
            num2 = int(input("Enter second side: "))
            result = math.sqrt((num1 ** 2) + (num2 ** 2))
            print(result)
            break

        if q == "SIDE":
            num1 = int(input("Enter hyp: "))
            num2 = int(input("Enter side: "))
            result = math.sqrt((num2 ** 2) - (num1 ** 2))
            print(result)
            break

        if q == "":
            continue

        else:
            print("Please input SIDE or HYP")
            continue

def rand():
    global result
    num1 = int(input("Enter minimum: "))
    num2 = int(input("Enter maximum: "))
    result = random.randint(num1, num2)
    print(result)

def avg():
    global result
    list_grab = []
    total = 0
    while True:
        try:
            num1 = int(input("Enter Number: "))
            list_grab.append(num1)
            total += 1
            continue
        except ValueError:
            break
    result = (sum(list_grab)) / total
    print(result)

def median():
    global result
    list_grab = []
    total = 0
    while True:
        try:
            num1 = int(input("Enter Number: "))
            list_grab.append(num1)
            total += 1
            continue
        except ValueError:
            break
    list_grab.sort()
    if len(list_grab) % 2 == 0:
        mid = total / 2
        result = (sum(list_grab)) / mid
    else:
        mid = len(list_grab) // 2
        mid1, mid2 = list_grab[mid - 1], list_grab[mid]
        result = (mid1 + mid2) / 2
    print(result)

#Dimensions

def peri():
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "SQUARE":
            num1 = int(input("Enter sides: "))
            result = 4 * num1
            print(result)
            break

        if q == "RECTANGLE":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            result = 2 * (num1 * num2)
            print(result)
            break

        if q == "TRIANGLE":
            num1 = int(input("Side 1 length: "))
            num2 = int(input("Side 2 length: "))
            num3 = int(input("Side 3 length: "))
            result = num1 + num2 + num3
            print(result)
            break

        if q == "PARALLELOGRAM":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = 2 * (num1 * num2)
            print(result)
            break

        if q == "TRAPEZOID":
            num1 = int(input("Enter side 1: "))
            num2 = int(input("Enter side 2: "))
            num3 = int(input("Enter side 3: "))
            num4 = int(input("Enter side 4: "))
            result = num1 + num2 + num3 + num4
            print(result)
            break

        if q == "RHOMBUS":
            num1 = int(input("Enter side: "))
            result = num1 * 4
            print(result)
            break

        if q == "CIRCLE":
            num1 = int(input("Enter radius: "))
            result = 2 * 3.1415 * num1
            print(result)
            break

        if q == "POLYGON":
            num1 = int(input("How many sides does your pentagon have?: "))
            num2 = int(input("What is the side length?: "))
            result = num1 * num2
            print(result)
            break

        if q == "":
            continue

        if q == "SHAPES":
            print('''
            Square
            Rectangle
            Triangle
            Paralellogram
            Trapezoid
            Rhombus
            Circle
            Polygon (Pentagon, Hexagon, ETC.)
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

def area():
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "SQUARE":
            num1 = int(input("Enter sides: "))
            result = num1 ** 2
            print(result)
            break

        if q == "RECTANGLE":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            result = num1 * num2
            print(result)
            break

        if q == "TRIANGLE":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = (num1 * num2) / 2
            print(result)
            break

        if q == "PARALLELOGRAM":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = num1 * num2
            print(result)
            break

        if q == "TRAPEZOID":
            num1 = int(input("Enter base 1: "))
            num2 = int(input("Enter base 2: "))
            num3 = int(input("Enter height: "))
            result = ((num1 + num2) / 2) * num3
            print(result)
            break

        if q == "RHOMBUS":
            num1 = int(input("Enter diagnol 1: "))
            num2 = int(input("Enter diagnol 2: "))
            result = (num1 * num2) / 2
            print(result)
            break

        if q == "CIRCLE":
            num1 = int(input("Enter radius: "))
            result = 3.1415 * (num1 ** 2)
            print(result)
            break

        if q == "POLYGON":
            num1 = int(input("How many sides does your pentagon have?: "))
            num2 = int(input("What is the side length?: "))
            num3 = int(input("What is the apothem length?: "))
            result = (num1 * num2 * num3) / 2
            print(result)
            break

        if q == "":
            continue

        if q == "SHAPES":
            print('''
            Square
            Rectangle
            Triangle
            Paralellogram
            Trapezoid
            Rhombus
            Circle
            Polygon (Pentagon, Hexagon, ETC.)
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

def sura():  # Find Surface Area
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "CUBE":
            num1 = int(input("Enter sides: "))
            result = 6 * (num1 ** 2)
            print(result)
            break

        if q == "RECTANGULAR PRISM":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            num3 = int(input("Enter height: "))
            result = 2 * ((num1 * num2) + (num1 * num3) + (num2 * num3))
            print(result)
            break

        if q == "RECTANGULAR PYRAMID":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            b = num1 * num2
            result = (2 * num3 * b) + b ** 2
            result = (num1 * num2 * num3) / 3
            print(result)
            break

        if q == "TRIANGULAR PRISM":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            b = (num1 * num2) / 2
            result = (b * num3) / 2
            print(result)
            break

        if q == "SPHERE":
            num1 = int(input("Enter Radius: "))
            result = 4 * 3.1415 * (num1 ** 2)
            print(result)
            break

        if q == "CYLINDER":
            num1 = int(input("Enter Radius: "))
            num2 = int(input("Enter Height: "))
            result = (2 * 3.1415 * (num1 ** 2)) + (2 * 3.1415 * num1 * num2)
            print(result)
            break

        if q == "":
            continue

        if q == "SHAPES":
            print('''
            Cube
            Rectangular Prism
            Triangular Prism
            Rectangular Pyramid
            Cylinder
            Sphere
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

def vol(): #Find Volume
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "CUBE":
            num1 = int(input("Enter sides: "))
            result = num1 ** 3
            print(result)
            break

        if q == "RECTANGULAR PRISM":
            num1 = int(input("Enter side 1: "))
            num2 = int(input("Enter side 2: "))
            num3 = int(input("Enter side 3: "))
            result = num1 * num2 * num3
            print(result)
            break

        if q == "RECTANGULAR PYRAMID":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            result = (num1 * num2 * num3) / 3
            print(result)
            break

        if q == "TRIANGULAR PRISM":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            result = ((num1 * num2) / 2 ) * num3
            print(result)
            break

        if q == "SPHERE":
            num1 = int(input("Enter Radius: "))
            result = 4/3 * math.pi * (num1 ** 3)
            print(result)
            break

        if q == "CYLINDER":
            num1 = int(input("Enter Radius: "))
            num2 = int(input("Enter Height: "))
            result = ((num1 ** 2) * 3.14) * num2
            print(result)
            break

        if q == "":
            continue

        if q == "SHAPES":
            print('''
            Cube
            Rectangular Prism
            Triangular Prism
            Rectangular Pyramid
            Cylinder
            Sphere
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

#Memory access (WIP)

def memsave():
    global m1
    m1 = result
    print(f"Saved {m1} to memory")

def memload():
    global m1
    print(m1)
