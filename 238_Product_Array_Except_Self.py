# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation

# TC: O(n)
# SC: O(n)

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        pref , suff, res = [0]*n, [0]*n , [0]* n
        pref[0] = 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = pref[i-1]* nums[i-1]
        
        for i in range(n-2, -1,-1):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
    

solution = Solution()
nums = [1,2,4,6]
print(solution.productExceptSelf(nums))