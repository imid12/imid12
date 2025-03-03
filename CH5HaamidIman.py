'''
MPG Calculator - This script calculates and prints the miles per gallon (MPG) for multiple cars.
Functionality:
    Initialization:
        initialMiles: Stores the initial odometer reading. Initialized to 1 to start the loop.
        count: Tracks the car number, starting from 1.
    Looping for Input:
        Inside the loop, the user is prompted to enter the initial odometer reading.
    Termination Condition:
        If the user enters a negative number for initialMiles, the loop breaks, ending the program.
    Calculating and Displaying MPG:
        If initialMiles is positive, the user is prompted to enter the final odometer reading and the number of gallons of gas used.
        The MPG is calculated using the formula: (finalMiles - initialMiles) / gallons.
        The calculated MPG and the car number are printed to the console.
        The count is incremented by 1 to prep
'''

initialMiles = 1 
count = 1
#   A while loop continues as long as initialMiles is greater than 0
while initialMiles > 0:
    initialMiles = int(input("Initial odometer reading: "))
    if initialMiles < 0:
        break
    else:   
        finalMiles = int(input("Final odometer reading: "))
        gallons = int(input("Number of gallons of gas: "))
        mpg = (finalMiles - initialMiles) / gallons
        print("Miles per Gallon of Car #",count, ":", mpg)
        count += 1
