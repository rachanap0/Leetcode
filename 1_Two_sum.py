
# Brute force approach
# # TC: O(n^2) where n is number of elements in the array

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

# Example usage:
solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums, target))  # Output: [0, 1]


# nums = [2,7,11,15]
# target = 9
# 2 -> 0
# 7 -> 1
# 11 ->3
# 15 -> 4

# Optimized approach using a hash map 
# TC: O(n) where n is number of elements in the array
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}

        for i, n in enumerate(nums):
            dict[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict and dict[diff] != i:
                return [i, dict[diff]]
        return []
    
solution = Solution()
nums = [2,7,11,15]
target = 9
print(solution.twoSum(nums,target))

# Further optimized approach using a single pass hash map
# TC: O(n) where n is number of elements in the array
class Solution:
    def twoSum(self, nums, target):
        dict ={}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dict:
                return[dict[diff], i]
            dict[n] = i
        return []
    
solution = Solution()
nums = [4,5,6]
target = 10
print(solution.twoSum(nums, target))