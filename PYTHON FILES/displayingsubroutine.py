salboard=[["43", "44", "45", "46", "47", "48", "49"],
          ["42", "41", "40", "39", "38", "37", "36"],
          ["29", "30", "31", "32", "33", "34", "35"],
          ["28", "27", "26", "25", "24", "23", "22"],
          ["15", "16", "17", "18", "19", "20", "21"],
          ["14", "13", "12", "11", "10", "9", "8"],
          ["1", "2", "3", "4", "5", "6", "7"]]
import snakesandladders as sl

def disp(salboard, player_1total, player_2total):
    counter=0
    for row in salboard:
        display_row = []
        for item in row:
            item_num = int(item)
            if item_num == player_1total and item_num == player_2total:
                display_row.append("Both")
            elif item_num == player_1total:
                display_row.append("♔")
            elif item_num == player_2total:
                display_row.append("♞")
            else:
                display_row.append(item)
        print(" | ".join(display_row))
    print("\n")


#player_1total, player_2total=sl.s_lad()

#disp(salboard, player_1total, player_2total)

