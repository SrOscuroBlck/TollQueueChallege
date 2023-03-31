from Queue import Queue, arrival
from specialBehaviors import getCabinWithMostEarnings, sweepTypeOfCar
import random
import os

def randomCarType():
    return random.choice(['Car', 'Van', 'Truck', 'Bus'])

firstToll = Queue()
secondToll = Queue()
thirdToll = Queue()

def arrivalToFirstToll():
    arrival(firstToll, randomCarType())
    
def arrivalToSecondToll():
    arrival(secondToll, randomCarType())

def arrivalToThirdToll():
    arrival(thirdToll, randomCarType())
    
def randomArrival():
    random.choice([arrivalToFirstToll, arrivalToSecondToll, arrivalToThirdToll])()
    
for i in range(30):
    randomArrival()
    
print("=================================================")
print("> [1] - Toll cabin with most earnings.\n> [2] - Types of vehicles in each toll\n> [0] - Exit")
print("=================================================\n")


auxOp = "not empty"
op = int(input("Select an option "))
while op != 0:
    if op == 1:
        print('\n'*100)
        os.system('cls' if os.name == 'nt' else 'clear')
        while auxOp != "":
            print("\n[1] - Toll cabin with most earnings.\n")
            maxEarnings = getCabinWithMostEarnings(firstToll, secondToll, thirdToll)
            print(f"The cabin with most earnings was {maxEarnings['Cabin']}, with {maxEarnings['Earnings']}")
            auxOp = input("\nPress enter to go back to menu")
        
        auxOp = "not empty"
        
    elif op == 2:
        print('\n'*100)
        os.system('cls' if os.name == 'nt' else 'clear')
        while auxOp != "":
            print("\n[2] - Types of vehicles in each toll")
            for i in range(3):
                if i == 0:
                    print("\nFirst Toll")
                    sweepTypeOfCar(firstToll)
                elif i == 1:
                    print("\nSecond Toll")
                    sweepTypeOfCar(secondToll)
                else:
                    print("\nThird Toll")
                    sweepTypeOfCar(thirdToll)
                
            auxOp = input("\nPress enter to go back to menu")
        auxOp = "not empty"
        
    elif op == 0:
        break
        
    else:
        print("Wrong option")
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=================================================")
    print("> [1] - Toll cabin with most earnings.\n> [2] - Types of vehicles in each toll\n> [0] - Exit")
    print("=================================================\n")    
    op = int(input("Select an option "))