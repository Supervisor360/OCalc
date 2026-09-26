import math
import random
import os

ver = "v1.2" #Version Number
result = 0 #Result of the answer
memory = 0 #Memory (Saved Result)

#Misc Functions
def prompt(): #Help
    print('''
NOTE: Commands are not case sensitive.

Available commands & Functions:
======================================
QUIT - Quit/Exit Program
ABOUT - Information about the Program
CLEAR - Clear Screen
MLOAD - Load from Memory
MSAVE - Save to Memory
MCLEAR - Clear Memory (Back to 0)
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
TRIG - Trigonometry (WIP)
PYTH - Pythagorian Theorem (WIP)
AREA - Find Area
PERI - Find Perimeter
VOLU - Find Volume
SURA - Find Surface Area
======================================
    ''')
    return

def close(): #Quit Program
    print("Exiting Program")
    exit()

def about(): #About the program
    global ver
    print(f"OCalc {ver} by Regnbuebörk (Started 21/5/2026)")
    print("This is an Open Source multi-function & multi-purpose calculator program written entirely by one person in Python (NO AI) using PyCharm. It was mainly done to test my abilities in Python, as well as the fact I do not like most calculator programs and prefer the CLI interface. This program is intended to be published on pip and such for public usage and evaluation. Do note the program is very early in development and I am a beginner in Python. Thus, several functions may be incorrect and bugs may populate the code, despite my attempts to repair them. If you encounter any issues, please note them in the github and give me time to review, fix, and update the code and github repository with newer versions.")

def clear(): #Clear Screen
    # noinspection PyDeprecation
    os.system('cls' if os.name == 'nt' else 'clear')
    print("REGNBUEBÖRK Software 2026 - OCalc")
    print('Type HELP for a list of commands')

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
 while True:
    miss = input("Are you looking for DEGREE or SIDE?: ").upper()

    if miss == "DEGREE":

     while True:
        sct = input("Enter Ratio (Type HELP for a list of ratios): ").upper()

        if sct == "SIN":
            num1 = int(input("Enter Opposite "))
            num2 = int(input("Enter Hypotenuse "))
            result = math.asin(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")

        if sct == "COS":
            num1 = int(input("Enter Adjacent "))
            num2 = int(input("Enter Hypotenuse "))
            result = math.acos(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")
            break
        if sct == "TAN":
            num1 = int(input("Enter Opposite "))
            num2 = int(input("Enter Adjacent "))
            result = math.atan(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")
            break
        if sct == "SEC":
            num1 = int(input("Enter Hypotenuse "))
            num2 = int(input("Enter Adjacent "))
            result = math.acos(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")
        if sct == "COT":
            num1 = int(input("Enter Adjacent "))
            num2 = int(input("Enter Opposite "))
            result = math.atan(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")
            break
        if sct == "CSC":
            num1 = int(input("Enter Hypotenuse "))
            num2 = int(input("Enter Opposite "))
            result = math.asin(num1 / num2)
            result = math.degrees(result)
            print(f"{result}°")
            break
        if sct == "CANCEL":
            break

        if sct == "QUIT":
            exit()

        if sct == "HELP":
            print('''
Available Ratios:
======================================
SIN - Sine
COS - Cosine
TAN - Tangent
CSC - Cosec
SEC - Second
COT - Cot
CANCEL - Cancel
======================================
             ''')
        if sct == "":
            continue
        else:
            continue



    if miss == "SIDE":
     while True:
        sct = input("Enter Ratio (Type HELP for a list of ratios): ").upper()

        if sct == "SIN":
         while True:

             func = input("Are you looking for opposite or hypotenuse?: ").upper()
             
             if func == "OPPOSITE":
              num1 = int(input("Enter Hypotenuse: "))
              num2 = int(input("Enter Angle Degrees: "))
              num2 = math.radians(num2)
              result = num1 * math.sin(num2)
              print(f"{result}°")
              break

             if func == "HYPOTENUSE":
              num1 = int(input("Enter Opposite : "))
              num2 = int(input("Enter Angle Degrees: "))
              num2 = math.radians(num2)
              result = num1 * math.sin(num2)
              print(f"{result}°")
              break

             else:
              continue

        if sct == "COS":
         while True:

             func = input("Are you looking for adjacent or hypotenuse?: ").upper()
             if func == "ADJACENT":
              num1 = int(input("Enter hypotenuse: "))
              num2 = int(input("Enter Angle Degrees: "))
              num2 = math.radians(num2)
              result = num1 * math.cos(num2)
              print(f"{result}°")
              break

             if func == "HYPOTENUSE":
              num1 = int(input("Enter adjacent: "))
              num2 = int(input("Enter Angle Degrees: "))
              num2 = math.radians(num2)
              result = num1 * math.cos(num2)
              print(f"{result}°")
              break

             else:
                 continue

        if sct == "TAN":
            while True:

                func = input("Are you looking for opposite or adjacent?: ").upper()
                if func == "OPPOSITE":
                    num1 = int(input("Enter adjacent: "))
                    num2 = int(input("Enter Angle Degrees: "))
                    num2 = math.radians(num2)
                    result = num1 * math.tan(num2)
                    print(f"{result}°")
                    break

                if func == "ADJACENT":
                    num1 = int(input("Enter opposite: "))
                    num2 = int(input("Enter Angle Degrees: "))
                    num2 = math.radians(num2)
                    result = num1 * math.tan(num2)
                    print(f"{result}°")
                    break

                else:
                    continue

        if sct == "CANCEL":
            break

        if sct == "QUIT":
            exit()

        if sct == "HELP":
            print('''
Available Ratios:
======================================
SIN - Sine
COS - Cosine
TAN - Tangent
CSC - Cosec
SEC - Second
COT - Cot
CANCEL - Cancel
======================================
             ''')
        if sct == "":
            continue
        else:
            continue
    if miss == "CANCEL":
        break

    else:
        continue





def pyth(): #Pythagorean Theorem
    while True:
        global result
        q = input("Input HYP or SIDE (Cancel to exit): ").upper()
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

        if q == "CANCEL":
            break

        if q == "QUIT":
            exit()

        if q == "":
            continue

        else:
            print("Please input SIDE or HYP")
            continue

def rand(): #Random Number
    global result
    num1 = int(input("Enter minimum: "))
    num2 = int(input("Enter maximum: "))
    result = random.randint(num1, num2)
    print(result)

def avg(): #Average Number
    global result
    print("Press [ENTER] with a clear input to continue.")
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

def median(): #Median
    global result
    print("Press [ENTER] with a clear input to continue.")
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

def peri(): #Find Perimeter
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "SQAR":
            num1 = int(input("Enter sides: "))
            result = 4 * num1
            print(result)
            break

        if q == "RECT":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            result = 2 * (num1 * num2)
            print(result)
            break

        if q == "TRIG":
            num1 = int(input("Side 1 length: "))
            num2 = int(input("Side 2 length: "))
            num3 = int(input("Side 3 length: "))
            result = num1 + num2 + num3
            print(result)
            break

        if q == "PARA":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = 2 * (num1 * num2)
            print(result)
            break

        if q == "TRAP":
            num1 = int(input("Enter side 1: "))
            num2 = int(input("Enter side 2: "))
            num3 = int(input("Enter side 3: "))
            num4 = int(input("Enter side 4: "))
            result = num1 + num2 + num3 + num4
            print(result)
            break

        if q == "ROMB":
            num1 = int(input("Enter side: "))
            result = num1 * 4
            print(result)
            break

        if q == "CIRC":
            num1 = int(input("Enter radius: "))
            result = 2 * 3.1415 * num1
            print(result)
            break

        if q == "POLY":
            num1 = int(input("How many sides does your pentagon have?: "))
            num2 = int(input("What is the side length?: "))
            result = num1 * num2
            print(result)
            break

        if q == "CANCEL":
            break

        if q == "QUIT":
            exit()

        if q == "":
            continue

        if q == "SHAPES":
            print('''
Available shapes:
======================================
SQAR - Square
RECT - Rectangle
TRIG - Triangle
PARA - Paralellogram
TRAP - Trapezoid
ROMB - Rhombus
CIRC - Circle
POLY - Polygon (Pentagon, Hexagon, ETC.)
CANCEL - Cancel prompt
======================================
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

def area(): #Find Area
    while True:
        global result
        q = input("Input Shape (Type Shapes for a list of shapes): ").upper()

        if q == "SQAR":
            num1 = int(input("Enter sides: "))
            result = num1 ** 2
            print(result)
            break

        if q == "RECT":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            result = num1 * num2
            print(result)
            break

        if q == "TRIG":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = (num1 * num2) / 2
            print(result)
            break

        if q == "PARA":
            num1 = int(input("Enter base: "))
            num2 = int(input("Enter height: "))
            result = num1 * num2
            print(result)
            break

        if q == "TRAP":
            num1 = int(input("Enter base 1: "))
            num2 = int(input("Enter base 2: "))
            num3 = int(input("Enter height: "))
            result = ((num1 + num2) / 2) * num3
            print(result)
            break

        if q == "ROMB":
            num1 = int(input("Enter diagnol 1: "))
            num2 = int(input("Enter diagnol 2: "))
            result = (num1 * num2) / 2
            print(result)
            break

        if q == "CIRC":
            num1 = int(input("Enter radius: "))
            result = 3.1415 * (num1 ** 2)
            print(result)
            break

        if q == "POLY":
            num1 = int(input("How many sides does your pentagon have?: "))
            num2 = int(input("What is the side length?: "))
            num3 = int(input("What is the apothem length?: "))
            result = (num1 * num2 * num3) / 2
            print(result)
            break

        if q == "CANCEL":
            break

        if q == "QUIT":
            exit()

        if q == "":
            continue

        if q == "SHAPES":
            print('''
Available shapes:
======================================
SQAR - Square
RECT - Rectangle
TRIG - Triangle
PARA - Paralellogram
TRAP - Trapezoid
ROMB - Rhombus
CIRC - Circle
POLY - Polygon (Pentagon, Hexagon, ETC.)
CANCEL - Cancel prompt
======================================
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

        if q == "RPRM":
            num1 = int(input("Enter length: "))
            num2 = int(input("Enter width: "))
            num3 = int(input("Enter height: "))
            result = 2 * ((num1 * num2) + (num1 * num3) + (num2 * num3))
            print(result)
            break

        if q == "RPYR":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            b = num1 * num2
            result = (2 * num3 * b) + b ** 2
            result = (num1 * num2 * num3) / 3
            print(result)
            break

        if q == "TPRM":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            b = (num1 * num2) / 2
            result = (b * num3) / 2
            print(result)
            break

        if q == "SPRE":
            num1 = int(input("Enter Radius: "))
            result = 4 * 3.1415 * (num1 ** 2)
            print(result)
            break

        if q == "CYLD":
            num1 = int(input("Enter Radius: "))
            num2 = int(input("Enter Height: "))
            result = (2 * 3.1415 * (num1 ** 2)) + (2 * 3.1415 * num1 * num2)
            print(result)
            break

        if q == "":
            continue

        if q == "CANCEL":
            break

        if q == "QUIT":
            exit()

        if q == "SHAPES":
            print('''
Available shapes:
======================================
CUBE - Cube
RPRM - Rectangular Prism
TPRM - Triangular Prism
RPYR - Rectangular Pyramid
CYLD - Cylinder
SPRE - Sphere
CANCEL - Cancel prompt
======================================
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

        if q == "RPRM":
            num1 = int(input("Enter side 1: "))
            num2 = int(input("Enter side 2: "))
            num3 = int(input("Enter side 3: "))
            result = num1 * num2 * num3
            print(result)
            break

        if q == "RPYR":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            result = (num1 * num2 * num3) / 3
            print(result)
            break

        if q == "TPRM":
            num1 = int(input("Enter Base Width: "))
            num2 = int(input("Enter Base Length: "))
            num3 = int(input("Enter Height: "))
            result = ((num1 * num2) / 2 ) * num3
            print(result)
            break

        if q == "SPRE":
            num1 = int(input("Enter Radius: "))
            result = 4/3 * math.pi * (num1 ** 3)
            print(result)
            break

        if q == "CYLD":
            num1 = int(input("Enter Radius: "))
            num2 = int(input("Enter Height: "))
            result = ((num1 ** 2) * 3.14) * num2
            print(result)
            break

        if q == "CANCEL":
            break

        if q == "QUIT":
            exit()

        if q == "SHAPES":
            print('''
Available shapes:
======================================
CUBE - Cube
RPRM - Rectangular Prism
TPRM - Triangular Prism
RPYR - Rectangular Pyramid
CYLD - Cylinder
SPRE - Sphere
CANCEL - Cancel prompt
======================================
            ''')
            continue

        else:
            print("Please input which shape you want. (Type List for a list of shapes)")
            continue

#Memory Functions

def memsave(): #Save to Memory
    global memory
    memory = result
    print(f"Saved {memory} to memory")

def memload(): #Load from Memory
    global memory
    print(memory)

def memclear(): #Clear Memory
    global memory
    memory = 0
    print("Memory Cleared")
