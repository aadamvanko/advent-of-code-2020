with open("input.txt") as file:
    lines = file.read().strip().split("\n")

max_id = 0
# lines = ["FFFFFFFLLL", "BBBBBBBRRR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
for line in lines:
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    id_ = row * 8 + column
    max_id = max(max_id, id_)
print(max_id)