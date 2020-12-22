from functools import reduce

with open("input.txt") as file:
    lines = file.read().strip().split("\n")

trees_counts = []
width = len(lines[0])
moves = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
for move in moves:
    trees = 0
    x = 0
    y = 0
    while y < len(lines):
        if lines[y][x % width] == "#":
            trees += 1
        y += move[1]
        x += move[0]
    trees_counts.append(trees)
print(reduce(lambda t1, t2: t1 * t2, trees_counts))