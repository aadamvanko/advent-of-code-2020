with open("input.txt") as file:
    nums = [int(line) for line in file.read().strip().split("\n")]

nums.append(0)
nums = sorted(nums)
nums.append(max(nums) + 3)
one_jolt_diff = 0
three_jolt_diff = 0

for i in range(len(nums) - 1):
    diff = nums[i + 1] - nums[i]
    if diff == 1:
        one_jolt_diff += 1
    elif diff == 3:
        three_jolt_diff += 1

print(one_jolt_diff * three_jolt_diff)