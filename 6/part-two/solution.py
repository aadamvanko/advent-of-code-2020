with open("input.txt") as file:
    lines = file.read().strip().split("\n")

suma = 0
group = set()
first_line = True
for line in lines:
    if line == "":
        first_line = True
        suma += len(group)
        group = set()
    else:
        if first_line:
            group = set(list(line))
            first_line = False
        else:
            group &= set(list(line))
suma += len(group)
print(suma)
    