# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]that sum to 0 such that i != j, i != k, and j != k.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

#Brute Force approach
# TC: O(n^3)
# SC: O(n)

def threeSum(nums):
    res = set()
    nums.sort()
    # print(nums)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] ==0:
                    tmp = [nums[i], nums[j], nums[k]]
                    # print(tmp)
                    res.add(tuple(tmp))
    return [list(val) for val in res]

#example usage
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

#Second approach: Two pointer approach
# TC: O(n^2)
# SC: O(n)

def threeSum_pointer(nums):
    nums.sort()
    res = []

    for i,a in enumerate(nums):
        #check if a is >0, if yes we stop as in an sorted array if the starting is positve then there can be no negative number moving forward to cancel it to 0
        if a>0:
            break

        if i>0 and a == nums[i-1]: #check if the previous element is the same as current, if yes drop the current element
            continue

        left = i+1 #to find b, start from after a
        right = len(nums)-1 #to find c, start from last
        while left<right:
            threeSum = a + nums[left]+ nums[right]

            if threeSum > 0:
                right -=1
            elif threeSum <0:
                left +=1
            else:
                res.append([a,nums[left], nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left -1]: #check if the incremented left is same as previous left, if yes increment left again
                    left +=1
    return res  

#example usage
nums = [-1,0,1,2,-1,-4]
print(threeSum_pointer(nums))   
            