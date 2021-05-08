with open("input.txt") as file:
    lines = file.read().strip().split("\n")

def run_program(lines):
    acc = 0
    i = 0
    visited = set()
    while 0 <= i < len(lines):
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
            return None

        if i == len(lines):
            return acc


for i in range(len(lines)):
    name, arg = lines[i].split()
    if name == "acc":
        continue

    old_line = lines[i]
    from_, to = "nop", "jmp"
    if name == "jmp":
        from_, to = to, from_
    lines[i] = lines[i].replace(from_, to)
    acc = run_program(lines)
    if acc is not None:
        print(acc)
    lines[i] = old_line