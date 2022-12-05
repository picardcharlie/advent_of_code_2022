"""
This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

# Input values are in a text document seperated by a single empty line.  Convert text into a list containing lists
# of each elfs calorie count.

# Then iterate through list adding totals up and saving the list location and total of most calories.

raw_input = open("day_one_input.txt", "r")

# iterate over each line of input.
current_number = 0
temp_number_string = ""
new_line = 0
current_total = 0
elf_list = []

for i in raw_input.read():
    # if it's a new line and there was just previously a new line,
    if i == '\n' and new_line == 1:
        elf_list.append(current_total)
        current_total = 0

    elif i == '\n' and new_line == 0:
        new_line = 1
        current_total += int(temp_number_string)
        temp_number_string = ""

    #elif i != '\n':
    else:
        temp_number_string += i
        new_line = 0

elf_list.append(current_total)

max_calories = 0
elf_location = 0
current_location = 0

for i in elf_list:
    current_location += 1
    if i > max_calories:
        max_calories = i
        elf_location = current_location

print(f"The elf carrying the most calories is number {elf_location} who is carrying {max_calories}.")

top3 = [0,0,0]

for i in elf_list:
    y = 0
    for x in top3:
        if i > x:
            top3[y] = i
            break
        y += 1

top3_total = 0
for x in top3:
    top3_total += x

print(f"The top three elves are carrying {top3[0]}, {top3[1]}, {top3[2]} calories.")
print(f"This is {top3_total} calories all together.")