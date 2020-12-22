with open("input.txt") as file:
    lines = file.read().strip().split("\n")
count = 0
for line in lines:
    rule, password = line.split(": ")
    count_part, letter = rule.split()
    from_, to = [int(token) for token in count_part.split("-")]
    if (password[from_ - 1] == letter and password[to - 1] != letter) or \
        (password[from_ - 1] != letter and password[to - 1] == letter):
        count += 1
print(count)