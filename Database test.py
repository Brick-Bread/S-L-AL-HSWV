
import csv

# THIS MOTHERFUCKING CODE DOESN'T WORK, IMA JUMP

salboard = [
    ["43", "44", "45", "46"],
    ["42", "41", "40", "39"],
    ["29", "30", "31", "32"],
    ["28", "27", "26", "25"],
    ["15", "16", "17", "18"],
    ["14", "13", "12", "11"],
    ["1", "2", "3", "4"]
    ]

table = salboard

"""with open('C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/winners.csv', 'w') as file: # This creates the new file dumbass
    writer = csv.writer(file)
    writer.writerow(["player 1", "Player 2"])

with open("C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/winners.csv", "r") as file: # This reads the csv file to print the row for testing purposes since I am the goat
    content = csv.reader(open("winners.csv"))
    header = next(content)"""



with open("C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/dice.csv", "w") as file: # This creates a new database file for the winners of the game if you are a retard and can't read simple code
    writer = csv.writer(file)
    writer.writerow(["Player 1", "Player 2"])

    for row in table:
        writer.writerow([f"{row[0]} {row[1]} {row[2]} {row[3]}"])   # SUP IMBECILES THIS PUTS THE DICE VALUES SIDE BY SIDE

# CSV file like a table format
with open("C:/Users/Josep/OneDrive/Desktop/Sixthform/2D array work/dice.csv", "r") as file:
    content = csv.reader(open("dice.csv"))
    header = next(content)

    # print the header (correct neat format)
    print(f"{header[0]:<20} {header[1]:<20}")
    print("-" * 40)

    # print each row (correct neat format)
    for row in content:
        if len(row) >= 2:
            print(f"{row[0]:<15} {row[1]:<15}")

