#correct

# TC: O(n^2) where n is number of elements in the array

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