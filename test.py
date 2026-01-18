nums = [1, 2, 3, 5, 4]
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        print(False)
else:
    print(True)