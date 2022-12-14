'''
.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other.
For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6.
In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively
cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration.
In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
'''

#first five inputs
# 14-50,14-50
# 43-44,43-87
# 55-99,51-96
# 67-68,68-91
# 8-8,  27-73

raw_input = open("day_four_input.txt", "r")

all_elf_pairs = []
elf_pair = []
quadrant = []
current_input = ""

for y in raw_input.read():
    if y == '\n':
        quadrant.append(int(current_input))
        elf_pair.append(quadrant)
        all_elf_pairs.append(elf_pair)
        elf_pair = []
        quadrant = []
        current_input = ""

    elif y == ',':
        quadrant.append(int(current_input))
        elf_pair.append(quadrant)
        quadrant = []
        current_input = ""

    elif y == '-':
        quadrant.append(int(current_input))
        current_input = ""

    else:
        current_input += y

# format = all pairs[ elf_duo[ elf1_range[start,finish], elf2_range[start,finish] ] ]

total_overlap = 0

for pair in all_elf_pairs:
    elf1 = pair[0]
    elf2 = pair[1]
    if elf1[0] <= elf2[0] <= elf2[1] <= elf1[1] or elf2[0] <= elf1[0] <= elf1[1] <= elf2[1]:
        total_overlap += 1

print(total_overlap)

'''
all the code that is too much
'''

#    elf1 = pair[0]
#    elf2 = pair[1]
#    compared_list1 = []
#    compared_list2 = []
#    contained_section = None
#    for section1 in range(elf1[0],(elf1[1])+1):
#        if section1 in range(elf2[0],(elf2[1])+1):
#            compared_list1.append(section1)
#
#    #if compared_list1 == elf1:
#    #    total_overlap += 1
#    #    compared_list1 = []
#
#    for section2 in range(elf2[0], elf2[1]+1):
#        if section2 in range(elf1[0], elf1[1]+1):
#            compared_list2.append(section2)
#
#    if compared_list1 == elf1 or compared_list2 == elf2:
#        total_overlap += 1
#        print(compared_list1, compared_list2)
#    compared_list1 = []
#    compared_list2 = []

