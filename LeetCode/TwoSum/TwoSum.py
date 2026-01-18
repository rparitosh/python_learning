def twoSum(nums,target):

    sum = 0
    pointer1 = 0
    pointer2 = 1
    found = False
    while  pointer1 < len(nums):
        sum = nums[pointer1] + nums[pointer2]
        if sum == target:
            found = True
            break
        if pointer2 == len(nums) - 1:
            pointer1 += 1
            pointer2 = pointer1 + 1
        else:
            pointer2 += 1
    if found:
        return ([pointer1, pointer2])


print (twoSum([0,0,1,2],1))
