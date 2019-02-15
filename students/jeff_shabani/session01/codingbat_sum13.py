def sum13(nums):
    for i in range(0, len(nums)):
        if nums[i] == 13:
            if i == len(nums)-1:
                nums.pop()
            else:
                nums[i] = 0
                nums[i+1] = 0
    return sum(nums)