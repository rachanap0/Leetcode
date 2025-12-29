# remove duplicate from a sorted array in place
# eg nums = [1,1,2] => return length = 2, nums = [1,2,_]
# eg nums = [0,0,1,1,1,2,2,3,3,4] => return length = 5, nums = [0,1,2,3,4,_,_,_,_,_]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        j = 0 #initializing a pointer to point to a unique value
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j +=1
                nums[j] = nums[i] #overwrite the value 
        return j+1  #as it started at the index
    
solution = Solution()
print(solution.removeDuplicates([1,1,2,2,3,4,5]))