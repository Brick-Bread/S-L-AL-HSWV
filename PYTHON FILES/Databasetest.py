
import csv

# THIS MOTHERFUCKING CODE DOESN'T WORK, IMA JUMP

# It now works I guess, will work on putting into subroutines tomorrow

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

winner_P = input("Who was the winner?: ")

winner = []
winner.append(winner_P)

with open("databases/winners.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow([winner_P])

"""with open('databases/winners.csv', 'w') as file: # This creates the new file dumbass
    writer = csv.writer(file)
    writer.writerow(["player 1", "Player 2"])

with open("databases/winners.csv", "r") as file: # This reads the csv file to print the row for testing purposes since I am the goat
    content = csv.reader(open("winners.csv"))
    header = next(content)"""



with open("databases/dice.csv", "w") as file: # This creates a new database file for the winners of the game if you are a retard and can't read simple code
    writer = csv.writer(file)
    writer.writerow(["Player 1", "Player 2"])

    for row in table:
        writer.writerow([f"{row[0]} {row[1]}", f"{row[2]} {row[3]}"])   # SUP IMBECILES THIS PUTS THE DICE VALUES SIDE BY SIDE

# CSV file like a table format
with open("databases/dice.csv", "r") as file:
    content = csv.reader(file)
    header = next(content)

    # print the header (correct neat format)
    print(f"{header[0]:<20} {header[1]:<20}")
    print("-" * 40)

    # print each row (correct neat format)
    for row in content:
        if len(row) >= 2:
            print(f"{row[0]:<20} {row[1]:<20}")
