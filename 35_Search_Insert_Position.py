#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.


def searchInsert(self, nums, target):
    if not nums:
        return 0
    
    length = len(nums)
    for i in range(length):
        if nums[i] >= target:
            return i
    return length

nums = [1,3,4,5,6,8,9,10]
target = 7
print(searchInsert(None, nums, target))  # Output: 5