nums = [1, 4, 7, 13, 17]

new_num = int(input("Add a new number"))

for i in range(len(nums)):
    if new_num < nums[i]:
        nums.insert(i, new_num)
        break
print(nums)


