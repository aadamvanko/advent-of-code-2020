with open("input.txt") as file:
    numbers = [int(line) for line in file.read().strip().split("\n")]

window_size = 25
window = numbers[:25]
for n in numbers[25:]:
    is_possible = False
    for a in window:
        for b in window:
            if a + b == n:
                is_possible = True
    if not is_possible:
        print(n)
        break
    window.append(n)
    window = window[1:]