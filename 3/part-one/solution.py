with open("input.txt") as file:
    lines = file.read().strip().split("\n")
x = 0
y = 0
trees = 0
width = len(lines[0])
while y < len(lines):
    if lines[y][x % width] == "#":
        trees += 1
    y += 1
    x += 3
print(trees)