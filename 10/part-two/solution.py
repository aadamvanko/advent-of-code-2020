with open("input.txt") as file:
# with open("input_small_2.txt") as file:
# with open("input_small.txt") as file:
    nums = [int(line) for line in file.read().strip().split("\n")]


def is_valid(path, device):
    path = path[:]
    path.insert(0, 0)
    path.append(device)

    for i in range(len(path) - 1):
        diff = path[i + 1] - path[i]
        if diff >= 4:
            # print("BIG DIFF", diff, path[i + 1], path[i])
            return False
    return True

count = 0
nums.sort()
device = max(nums) + 3

visited = set()
def find_all(path, f):
    if not is_valid(path, device):
        return

    #visited.add(tuple(path))
    global count
    count += 1
    # print(visited, path)
    for i in range(f, len(path)):
        sub = path[:i] + path[i + 1:]
        # print(sub)
        find_all(sub, i)


find_all(nums, 0)

for i in range(1, len(nums)):


print(count)