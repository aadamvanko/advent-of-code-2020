with open("input.txt") as file:
    lines = file.read().strip().split("\n")
count = 0
for line in lines:
    rule, password = line.split(": ")
    count_part, letter = rule.split()
    from_, to = [int(token) for token in count_part.split("-")]
    if from_ <= password.count(letter) <= to:
        count += 1
print(count)