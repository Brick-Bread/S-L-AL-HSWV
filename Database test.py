
import csv 

with open('C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/dice.csv', 'w') as file: # This creates the new file dumbass
    writer = csv.writer(file)
    writer.writerow(["player 1", "Player 2"])

with open("C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/dice.csv", "r") as file: # This reads the csv file to print the row for testing purposes since I am the goat
    content = csv.reader(open("dice.csv"))
    header = next(content)

    print(header)

