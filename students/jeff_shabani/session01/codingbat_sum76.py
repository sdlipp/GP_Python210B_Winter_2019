def sum67(nums):
    result = list()
    if 6 not in nums or 7 not in nums:
        result = nums
    for i in range(0, len(nums)-1):
        #check if 6 is immediately followed by 7
        if nums[i] == 6:
            if nums[i+1]==7:
                nums[i] = 0
                nums[i+1] = 0
                result = nums
            # check if 7 last list item
            elif nums[::-1][0] == 7:
                if 6 not in nums[nums.index(6)+1:nums.index(7)+1]:
                    #slice list item 6 through the end oflist.
                    new = nums[nums.index(6):nums.index(7)+1]
                    #list comprehension of nums items not in new above
                    result = ([i for i in nums if i not in new])
                    return result
    return result