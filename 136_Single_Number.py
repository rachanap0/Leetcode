# Given a non empty array of integers nums, every element appears twice except for one. Find that single one.

#time complexity is O(n) where n is number of elements in the array
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for num in nums:
        result ^= num #XOR operation removes all duplicates
    return result


# Example usage:
nums = [4,1,2,1,2]
print(singleNumber(nums))  # Output: 4