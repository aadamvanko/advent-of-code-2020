with open("input.txt") as file:
    lines = file.read().strip().split("\n")

suma = 0
group = set()
for line in lines:
    if line == "":
        suma += len(group)
        group = set()
    else:
        group |= set(list(line))
suma += len(group)
print(suma)
    