import re

with open("input.txt") as file:
    lines = file.read().strip().split("\n")


def is_valid(passport):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    for field in required_fields:
        if field not in passport:
            return False
    return True


def is_number(s):
    try:
        int(s)
        return True
    except:
        return False


def has_valid_values(passport):
    byr = passport["byr"]
    if not (is_number(byr) and 1920 <= int(byr) <= 2002):
        return False
    
    iyr = passport["iyr"]
    if not (is_number(iyr) and 2010 <= int(iyr) <= 2020):
        return False
    
    eyr = passport["eyr"]
    if not (is_number(eyr) and 2020 <= int(eyr) <= 2030):
        return False

    hgt = passport["hgt"]
    match = re.match(r"([0-9]+)([a-z]+)$", hgt)
    if not match:
        return False 
    value, unit = match.groups()
    if not is_number(value):
        return False
    if not ((unit == "in" and 59 <= int(value) <= 76) or (unit == "cm" and 150 <= int(value) <= 193)):
        return False

    ecl = passport["ecl"]
    if ecl not in "amb blu brn gry grn hzl oth".split():
        return False

    hcl = passport["hcl"]
    if not re.match(r"#[0-9a-f]{6}$", hcl):
        return False

    pid = passport["pid"]
    if not re.match(r"\d{9}$", pid):
        return False

    return True

passport = {}
count = 0
for line in lines:
    if line == "":
        if is_valid(passport) and has_valid_values(passport):
            count += 1
        passport = {}
        continue
    
    for pair in line.split():
        key, value = pair.split(":")
        passport[key] = value

if is_valid(passport) and has_valid_values(passport):
    count += 1
print(count)