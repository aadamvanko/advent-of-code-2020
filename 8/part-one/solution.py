with open("input.txt") as file:
    lines = file.read().strip().split("\n")

acc = 0
i = 0
visited = set()
while True:
    visited.add(i)
    name, arg = lines[i].split()
    arg = int(arg)
    if name == "acc":
        acc += arg
        i += 1
    elif name == "jmp":
        i += arg
    else:
        i += 1

    if i in visited:
        print(acc)
        break
