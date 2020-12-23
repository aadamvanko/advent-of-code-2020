with open("input.txt") as file:
    lines = file.read().strip().split("\n")


def rec_count(rules, from_):
    if from_ not in rules:
        return 0

    suma = 1
    for rule in rules[from_]:
        count = max(rule[0] * 1, rule[0] * rec_count(rules, rule[1]))
        suma += count
    return suma


rules = {}
for i, line in enumerate(lines):
    line = line[:-1]
    type_, parts = line.split("contain ")
    type_ = type_.split("bags")[0].strip()

    parts = parts.split(",")
    definitions = []
    if parts[0] == "no other bags":
        pass
    else:
        for part in parts:
            part = part.strip()
            if part == "":
                pass
            num, *other_type = part.split()[:3]
            definition = (int(num), ' '.join(other_type))
            definitions.append(definition)
        rules[type_] = definitions

count = rec_count(rules, "shiny gold") - 1
print(count)