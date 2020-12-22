with open("input.txt") as file:
    lines = file.read().strip().split("\n")

max_id = 0
# lines = ["FFFFFFFLLL", "BBBBBBBRRR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
ids = set()
for line in lines:
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    id_ = row * 8 + column
    ids.add(id_)

for id_ in range(min(ids), max(ids) + 1):
    i = id_
    pi = i - 1
    ni = i + 1
    if i not in ids and pi in ids and ni in ids:
        print(i)