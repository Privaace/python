def find_dup(nums):
    freq={}
    for n in nums:
        if n in freq:
            return True
        else:
            freq[n]=1
            
print(find_dup([1, 2, 3, 1]))