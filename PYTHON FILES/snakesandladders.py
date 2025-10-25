salboard=[["43", "44", "45", "46", "47", "48", "49"],
      ["42", "41", "40", "39", "38", "37", "36"],
      ["29", "30", "31", "32", "33", "34", "35"],
      ["28", "27", "26", "25", "24", "23", "22"],
      ["15", "16", "17", "18", "19", "20", "21"],
      ["14", "13", "12", "11", "10", "9", "8"],
      ["1", "2", "3", "4", "5", "6", "7"]]

# DISPLAY ISSUE
import Databasetest as ballz
import csv
import random
import displayingsubroutine as ds
def s_lad():
  player_1total = 0
  player_2total = 0
  round_num = 0
  winner = ""



  player_1total = 0 # equivilent to position
  player_2total = 0 # equivilent to position
  prompt1 = 0 # used to prompt user to roll dice
  prompt2 = 0 # used to prompt user to roll dice
  round_num = 0 # used to count rounds
  # intro to game and rules
  print("Welcome to Snakes and Ladders")
  print("===================================")
  print("here are the rules:")
  print("====================================")
  print("1) Two players take turns to roll two dice and move their piece forward the amount rolled")
  print("2) If you roll a double, you go back the amount you rolled")
  print("====================================")
  print("3) If you land on a ladder, you move up to the higher number")
  print("Ladders: 3 to 22, 5 to 8, 11 to 26, 20 to 29")
  print("====================================")
  print("4) If you land on a snake, you move down to the lower number")
  print("Snakes: 17 to 4, 19 to 7, 27 to 1, 39 to 3")
  print("====================================")
  print("*IMPORTANT* First player to reach 49 wins:)")
  
  # main game loop which continues until one player reaches 49
  
  ladder1=random.randint(8,49)
  ladder2=random.randint(8,49)
  ladder3=random.randint(15,49)
  ladder4=random.randint(22,49)
  snake1=random.randint(1,14)
  snake2=random.randint(1,14)
  snake3=random.randint(1,21)
  snake4=random.randint(1,35)

  while player_1total < 49 and player_2total < 49:
    round_num += 1 # counts rounds
    print(f"Round {round_num}") # shows round number
    
    prompt1 = input("Player 1, press enter to roll the dice") # prompts player 1 to  iniciate the rolling of both dices
    roll1 = random.randint(1,6) # rolls dice 1
    roll2 = random.randint(1,6) # rolls dice 2

    if roll1 == roll2: # checks if a double was rolled
      print(f"Double was rolled, you go back {roll1 + roll2} spaces") # informs player they rolled a double
      player_1total -= roll1 + roll2 # moves player back the amount rolled (look at the task we were given and it says we need to do this)
    print(f"Player 1 rolled a {roll1} and a {roll2}") # informs player of what they rolled
    player_1total += roll1 + roll2 # moves player forward the amount rolled
    

    if player_1total < 1: # checks if player position is below 1 (a failsafe from an error i encountered while testing)
      player_1total = 1 # sets player position to 1 if below 1 cah board starts from 1 to 49



    if player_1total > 49: # checks if player position is above 49
      player_1total = 49  # sets player position to 49 if above 49 as the board ends at 49 (again i encountered an error where when i had this a player would roll above 49 and it would break the game not display the win message and just end)
      
      print(f"player 1 is moving {roll1 + roll2} spaces") # informs player how many spaces they are moving

    if player_1total == 3: # checks if player landed on a ladder
      player_1total = 22 # moves player to the top of the ladder
      
      print("Player 1 climbed a ladder to ",ladder1)

    elif player_1total == 5:
      player_1total = 8
      
      print("Player 1 climbed a ladder to ",ladder2)

    elif player_1total == 11:
      player_1total = 26

      print("Player 1 climbed a ladder to ",ladder3)

    elif player_1total == 20:
      player_1total = 29

      print("Player 1 climbed a ladder to ",ladder4)

    elif player_1total == 17:  
      player_1total = 4
      print("Player 1 got bitten by a snake to ",snake1)

    elif player_1total == 19:
      player_1total = 7
      print("Player 1 got bitten by a snake to ",snake2)
      
    elif player_1total == 27:
      player_1total = 1
      print("Player 1 got bitten by a snake to ",snake3)

    elif player_1total == 39:
      
      player_1total = 3
      print("Player 1 got bitten by a snake to ",snake4) 

    ds.disp(salboard,player_1total,player_2total)

    if player_1total == 49: # checks if player 1 has won
      print("Player 1 wins!") # informs players that player 1 has won
      winner = "Player 1"
      print(f"player 2 was on {player_2total}") # informs players of player 2 position
      print("Game Over") # informs players that the game is over
      break # breaks the loop to end the game (defo didnt have to revise where to put breaks ......)
    
    #player 2 turn (same as player 1 but for player 2) all in same round
    
    prompt2 = input("Player 2, press enter to roll the dice") # prompts player 2 to  iniciate the rolling of both dices
    roll1 = random.randint(1,6) # rolls dice 1
    roll2 = random.randint(1,6) # rolls dice 2
    print(f"Player 2 rolled a {roll1} and a {roll2}")
    player_2total += roll1 + roll2
    
    if roll1 == roll2:
      print(f"Double was rolled, you go back {roll1 + roll2} spaces")
      player_2total -= roll1 + roll2
      

    if player_2total < 0:
      player_2total = 0
      

    if player_2total > 49:
      player_2total = 49
      

    if player_2total == 3:
      player_2total = ladder1
      
      print("Player 2 climbed a ladder to ",ladder1)

    elif player_2total == 5:
      player_2total = ladder2
      
      print("Player 2 climbed a ladder to ",ladder2)

    elif player_2total == 11:
      player_2total = ladder3
      
      print("Player 2 climbed a ladder to ",ladder3)

    elif player_2total == 20:
      player_2total = ladder4
      
      print("Player 2 climbed a ladder to ",ladder4)

    elif player_2total == 17:
      player_2total = snake1
      
      print("Player 2 got bitten by a snake to ",snake1)

    elif player_2total == 19:
      player_2total = snake2
      
      print("Player 2 got bitten by a snake to ",snake2)

    elif player_2total == 27:
      player_2total = snake3
      
      print("Player 2 got bitten by a snake to ",snake3)

    elif player_2total == 39:
      player_2total = snake4
      
      print("Player 2 got bitten by a snake to ",snake4)

    ds.disp(salboard, player_1total, player_2total)

    if player_2total == 49: # checks if player 2 has won
      print("Player 2 wins!")  # informs players that player 2 has won
      winner = "Player 2"
      print(f"player 1 was on {player_1total}") # informs players of player 1 position, if ur thinky why i dont show both player 2 and 1 position for this to run one player is at position 49 and the other player could be anywhere from 1 to 48 so i just show the other players position
      print("Game Over") # informs players that the game is over
      break 

    
  return(player_1total, player_2total, winner, round_num) # for the writing and whatever we need the results for idk , just returns the final positions of both players


game = s_lad() #yk what this does
print(game) 


player_1total, player_2total, winner, round_num = game

ballz.create_database() # only ever needed once
ballz.write_to_database(winner, round_num)

