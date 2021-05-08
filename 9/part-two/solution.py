with open("input.txt") as file:
    numbers = [int(line) for line in file.read().strip().split("\n")]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        sub = numbers[i:j]
        suma = sum(sub)
        if suma == 20874512:
            print(min(sub) + max(sub))
        elif suma > 20874512:
            break
