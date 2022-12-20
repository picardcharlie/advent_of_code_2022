import re

'''
From the starting stack of crates, follow the directions in moving the crates around.
Need to know which crates are on the top at the end.

        [F] [Q]         [Q]
[B]     [Q] [V] [D]     [S]
[S] [P] [T] [R] [M]     [D]
[J] [V] [W] [M] [F]     [J]     [J]
[Z] [G] [S] [W] [N] [D] [R]     [T]
[V] [M] [B] [G] [S] [C] [T] [V] [S]
[D] [S] [L] [J] [L] [G] [G] [F] [R]
[G] [Z] [C] [H] [C] [R] [H] [P] [D]
 1   2   3   4   5   6   7   8   9
 
 56

'''

# list of all crates
all_crates = [["G","D","V","Z","J","S","B"],\
              ["Z","S","M","G","V","P"],\
              ["C","L","B","S","W","T","Q","F"],\
              ["H","J","G","W","M","R","V","Q"],\
              ["C","L","S","N","F","M","D"],\
              ["R","G","C","D"],\
              ["H","G","T","R","J","D","S","Q"],\
              ["P","F","V"],\
              ["D","R","S","T","J"]]

#move 3 from 5 to 2
total_to_move = []
column_start = 0
column_end = 0
current_line = ""


raw_input = open("day_five_input.txt", "r")

for value in raw_input.read():

    if value == '\n':
        move = re.findall("[0-9][0-9]|[0-9]", current_line)
        total = int(move[0])
        start = int(move[1])
        end = int(move[2])

        column_to_move = all_crates[(start - 1)]

        total_to_move = column_to_move[-(total):]

        # Needs to append the last crate first and go back from there.
        # use for crate in reversed(total_to_move): to add them in reverse order.
        # part two does not do this, drop reversed.
        for crate in total_to_move:
            all_crates[(end - 1)].append(crate)

        for remove in range(len(total_to_move)):
            all_crates[(start - 1)].pop(-1)

        current_line = ""
        total_to_move = []
        column_to_move = []
        move = []

    else:
        current_line += value

for x in all_crates:
    print(x)