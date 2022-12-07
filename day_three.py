'''
Elves are giving out rucksacks full of stuff.  Each rucksack has two compartments, split equally by each input.

Each item has a priority list:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.

Sort each input and find the common item in both compartments and add the priority values of them all up.
'''

raw_input = open("day_three_input.txt", "r")

# iterate over each line of input.
rucksack_list = []
compartments = []
current_list = ""

for i in raw_input.read():
    # if it's a new line and there was just previously a new line,
    if i == '\n':
        compartments.append(current_list[:(len(current_list) // 2)])
        compartments.append(current_list[(len(current_list) // 2):])
        rucksack_list.append(compartments)
        compartments = []
        current_list = ""

    else:
        current_list += i

raw_input.close()

# sort those bags brother.  Check to see if the same letter is inside of each compartment.
# add value to total number.
total_checks = 0
current_total = 0
priority_values = { "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12,
                    "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23,
                    "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34,
                    "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42, "Q":43, "R":44, "S":45,
                    "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52 }

for rucksack in rucksack_list:
    compartment_one = rucksack[0]
    for item in compartment_one:
        compartment_two = rucksack[1]
        if item in compartment_two:
            total_checks += 1
            current_total += priority_values[item]
            #print(f"{compartment_one} + {compartment_two} + {item} + {total_checks}")
            break


print(f"Total priority score: {current_total} for item in each rucksack.")

raw_input2 = open("day_three_input.txt", "r")

rucksack_count = 0
rucksack_badges = []
current_list = ""
compartments = []
for i in raw_input2.read():
    # if it's a new line and there was just previously a new line,
    if i == '\n':
        compartments.append(current_list)
        rucksack_count += 1

        if rucksack_count == 3:
            rucksack_badges.append(compartments)
            compartments = []
            rucksack_count = 0

        current_list = ""

    else:
        current_list += i


priority_total2 = 0
for rucksacks in rucksack_badges:
    elf1 = rucksacks[0]
    for item2 in elf1:
        if item2 in rucksacks[1] and item2 in rucksacks[2]:
            priority_total2 += priority_values[item2]
            break

print(f"Total priority of the elf's badges: {priority_total2}.")