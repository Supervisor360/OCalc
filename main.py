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

 elif command == "TRIG": #Trigonometry
     trig()
     continue

 elif command == "PYTH": #Pythagorean Theorem
     pyth()
     continue

 elif command == "RAND": #Random Number
     rand()
     continue

 elif command == "AVRG": #Average
     avg()
     continue

 elif command == "MEDN": #Mean
     median()
     continue

 elif command == "PERI": #Volume
     peri()
     continue

 elif command == "AREA": #Volume
     area()
     continue

 elif command == "SURA": #Volume
     sura()
     continue

 elif command == "VOLU": #Volume
     vol()
     continue

 #Memory access (WIP)

 elif command == "MSAVE": #Pythagorean Theorem
     memsave()
     continue

 elif command == "MLOAD": #Pythagorean Theorem
     memload()
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

