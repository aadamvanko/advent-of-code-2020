with open("input.txt") as file:
    numbers = [int(token) for token in file.read().strip().split("\n")]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        for k in range(len(numbers)):
            if i != j and j != k and numbers[i] + numbers[j] + numbers[k] == 2020:
                print(numbers[i] * numbers[j] * numbers[k])
