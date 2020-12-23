with open("input.txt") as file:
    lines = file.read().strip().split("\n")


def can_reach_shiny_bag(rules, from_):
    if "shiny gold" in rules[from_]:
        return True
    else:
        for to in rules[from_]:
            if can_reach_shiny_bag(rules, to):
                return True
        return False


mapping = {}
rules = {}
shiny_bag_id = None
for i, line in enumerate(lines):
    line = line[:-1]
    type_, parts = line.split("contain")
    parts = parts.split(",")
    parts = [' '.join(p.split()[1:3]) for p in parts]
    type_ = type_.split("bags")[0].strip()
    rules[type_] = parts if parts[0] != "other bags" else []
    if type_ == "shiny gold":
        shiny_bag_id = i

count = 0
for type_ in rules:
    if can_reach_shiny_bag(rules, type_):
        count += 1
print(count)