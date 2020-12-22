with open("input.txt") as file:
    lines = file.read().strip().split("\n")


def is_valid(passport):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for field in required_fields:
        if field not in passport:
            return False
    return True


passport = {}
count = 0
for line in lines:
    if line == "":
        if is_valid(passport):
            count += 1
        passport = {}
        continue
    
    for pair in line.split():
        key, value = pair.split(":")
        passport[key] = value

if is_valid(passport):
    count += 1
print(count)