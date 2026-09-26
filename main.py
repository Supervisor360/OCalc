from commands import *
mistakes = 0

#Initial print
clear()

while True:
 command = input(f"CALC: ").upper()

 if command == "HELP": #Help
     prompt()
     continue

 elif command == "QUIT": #Quit
     close()
     continue

 elif command == "ABOUT": #Quit
     about()
     continue

 elif command == "CLEAR": #Clear screen
     clear()

 elif command == "MUL": #Multiplication
  mul()
  continue

 elif command == "DIV": #Division
  div()
  continue

 elif command == "ADD": #Addition
     add()
     continue

 elif command == "SUB": #Subtraction
     sub()
     continue

 elif command == "EXPO": #Exponentiate a number
     expo()
     continue

 elif command == "ROOT": #Root extraction
     root()
     continue

 elif command == "PERC": #Percentage
     perc()
     continue

 elif command == "TRIG": #Trigonometry (WIP)
     trig()
     continue

 elif command == "PYTH": #Pythagorean Theorem (WIP)
     pyth()
     continue

 elif command == "RAND": #Random Number
     rand()
     continue

 elif command == "AVRG": #Average
     avg()
     continue

 elif command == "MEDN": #Median
     median()
     continue

 elif command == "PERI": #Perimeter
     peri()
     continue

 elif command == "AREA": #Area
     area()
     continue

 elif command == "SURA": #Surface Area
     sura()
     continue

 elif command == "VOLU": #Volume
     vol()
     continue

 elif command == "MSAVE": #Save to memory
     memsave()
     continue

 elif command == "MLOAD": #Load from memory
     memload()
     continue

 elif command == "MCLEAR": #Clear memory
     memclear()
     continue

 #Non input Commands
 elif mistakes == 5:
     print('Type "HELP" for a list of commands')
     mistakes = 0
     continue

 #Unrecognized Input
 else:
     print("Command not found")
     mistakes += 1
     continue

