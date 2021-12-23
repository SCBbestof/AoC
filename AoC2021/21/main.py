from collections import defaultdict
from time import time
from functools import lru_cache

start = time()


players = [10, 4]
scores = [0, 0]


@lru_cache(maxsize=None)
def get_new_score(new_position, new_score):
    if new_position == 0:
        new_score += 10
    else:
        new_score += new_position
    return new_score


def process_rolls(cur_player, val):
    for die_roll, probability in probabilities.items():
        if cur_player == 0:
            new_position, new_score = (player1 + die_roll) % 10, score1
            new_score = get_new_score(new_position, new_score)
            next_states_map[(new_position, player2, new_score, score2)] += val * probability
        else:
            new_position, new_score = (player2 + die_roll) % 10, score2
            new_score = get_new_score(new_position, new_score)
            next_states_map[(player1, new_position, score1, new_score)] += val * probability


die_roll = 1
cur_player = 1
while scores[cur_player] < 1000:
    cur_player += 1
    cur_player %= 2
    players[cur_player] += ((die_roll + 1) * 3)
    players[cur_player] %= 10
    die_roll += 3

    scores[cur_player] = get_new_score(players[cur_player], scores[cur_player])


print("Part 1")
print("scores:", scores[0], scores[1])
print("score1:", scores[0] * (die_roll - 1))
print("score2:", scores[1] * (die_roll - 1))
end1 = time()

print()
print("Part 2")
probabilities = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}

states_map = {(10, 4, 0, 0): 1}
cur_player = 0

while True:
    next_states_map = defaultdict(int)
    for (player1, player2, score1, score2), val in states_map.items():
        if score1 < 21 and score2 < 21:
            process_rolls(cur_player, val)
        else:
            next_states_map[(player1, player2, score1, score2)] += val

    states_map = next_states_map
    cur_player += 1
    cur_player %= 2

    done = True
    for (player1, player2, score1, score2) in next_states_map.keys():
        if score1 < 21 and score2 < 21:
            done = False
            break
    if done:
        break


wins = [0, 0]
for (player1, player2, score1, score2), val in states_map.items():
    if score1 >= 21:
        wins[0] += val
    if score2 >= 21:
        wins[1] += val

print("wins (p1/p2):", wins)
print("max wins:", max(wins))
end2 = time()

print()
print("Execution time")
print("1:     " + str(end1 - start) + "s")
print("2:     " + str(end2 - end1) + "s")
print("Total: " + str(end2 - start) + "s")
