def second_largest(nums):
    largest=nums[0]
    second=nums[0]
    for n in nums:
        if n>largest:
            second=largest
            largest=n
        elif largest>n>second:
            second=n
    return second
print(second_largest([5, 1, 9, 7]))



