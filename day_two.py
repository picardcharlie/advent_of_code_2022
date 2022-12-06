'''
The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.

Your total score is the sum of your scores for each round. The score for a single round is the score for the
shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would
get if you were to follow the strategy guide.
'''

raw_input = open("day_two_input.txt", "r")

# iterate over each line of input.
cheatsheet_list = []
current_turn = []

for i in raw_input.read():
    # if it's a new line and there was just previously a new line,
    if i == '\n':
        cheatsheet_list.append(current_turn)
        current_turn = []

    elif i != ' ':
        current_turn.append(i)



# opponent is player 1    a=rock b=paper c=scissors
# lose=0 draw=3 win=6
# rock=1 paper=2 scissors=3
def rpc_results(turn_list):
    player_one = turn_list[0]
    player_two = turn_list[1]
    total_turn_score = 0

    # rock vs rock
    if player_one == "A" and player_two == "X":
        total_turn_score = 4

    # rock vs paper
    elif player_one == "A" and player_two == "Y":
        total_turn_score = 8

    # rock vs scissor
    elif player_one == "A" and player_two == "Z":
        total_turn_score = 3

    # paper vs rock
    elif player_one == "B" and player_two == "X":
        total_turn_score = 1

    # paper vs paper
    elif player_one == "B" and player_two == "Y":
        total_turn_score = 5

    # paper vs scissor
    elif player_one == "B" and player_two == "Z":
        total_turn_score = 9

    # scissor vs rock
    elif player_one == "C" and player_two == "X":
        total_turn_score = 7

    # scissor vs paper
    elif player_one == "C" and player_two == "Y":
        total_turn_score = 2

    # scissor vs scissor
    elif player_one == "C" and player_two == "Z":
        total_turn_score = 6

    return total_turn_score

def rpc_results_2(turn_list):
    player_one = turn_list[0]
    player_two = turn_list[1]
    total_turn_score = 0

    # x=lose y=draw z=win
    # opponent is player 1
    # a=rock b=paper c=scissors
    # lose=0 draw=3 win=6
    # rock=1 paper=2 scissors=3

    # rock vs lose
    if player_one == "A" and player_two == "X":
        total_turn_score = 3

    # rock vs draw
    elif player_one == "A" and player_two == "Y":
        total_turn_score = 4

    # rock vs win
    elif player_one == "A" and player_two == "Z":
        total_turn_score = 8

    # paper vs lose
    elif player_one == "B" and player_two == "X":
        total_turn_score = 1

    # paper vs draw
    elif player_one == "B" and player_two == "Y":
        total_turn_score = 5

    # paper vs win
    elif player_one == "B" and player_two == "Z":
        total_turn_score = 9

    # scissor vs lose
    elif player_one == "C" and player_two == "X":
        total_turn_score = 2

    # scissor vs draw
    elif player_one == "C" and player_two == "Y":
        total_turn_score = 6

    # scissor vs win
    elif player_one == "C" and player_two == "Z":
        total_turn_score = 7

    return total_turn_score

total_score = 0
for turn in cheatsheet_list:
    total_score += rpc_results(turn)

total_score_2 = 0
for turn in cheatsheet_list:
    total_score_2 += rpc_results_2(turn)

print(f"Total score following cheat sheet: {total_score}")

print(f"Total score the 2nd way: {total_score_2}")