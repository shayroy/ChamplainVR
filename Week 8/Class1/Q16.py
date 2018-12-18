nums=[10, 70, 20]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("The largest value is " + str(largest))

