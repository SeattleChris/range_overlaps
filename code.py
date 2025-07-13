#!/bin/python3

import os
from bisect import bisect_left, bisect_right
#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY shots
#  2. 2D_INTEGER_ARRAY players
#

def brute_solve(shots, players):
    """Solves in NxM time. Timeout on 8 test cases (17 - 24)"""
    return sum(
        1
        for (mn, mx) in players
        for (near, far) in shots if mn <= far and mx >= near
    )

def solve(shots, players):
    """Total sum of unique players overlap shot ranges."""
    starts, ends = [], []
    for (near, far) in shots:
        starts.append(near)
        ends.append(far)
    starts.sort()
    ends.sort()
    unders, overs = [], []
    for (mn, mx) in players:
        unders.append(bisect_left(ends, mn))
        overs.append(-1 * bisect_right(starts, mx))
    # Max possible - sum of each player's range being under or over shots.
    # return len(shots)*len(players) - sum(unders+overs) if overs use len(shots)
    return len(shots) * (len(players) - len(overs)) - sum(unders + overs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    shots = []
    for _ in range(n):
        shots.append(list(map(int, input().rstrip().split())))
    players = []
    for _ in range(m):
        players.append(list(map(int, input().rstrip().split())))
    result = solve(shots, players)
    fptr.write(str(result) + '\n')
    fptr.close()
