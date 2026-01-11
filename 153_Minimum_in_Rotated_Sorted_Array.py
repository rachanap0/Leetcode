# find the minimum element in a rotated sorted array 
# You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

# [3,4,5,6,1,2] if it was rotated 4 times.
# [1,2,3,4,5,6] if it was rotated 6 times.

#Brute Force approach
# TC: O(n)
# SC: O(1)
def findMin(nums):
    return min(nums)

#Example usage
nums = [3,4,5,1,2]
print(findMin(nums))  # Output: 1

#Optimized approach using Binary Search
# TC: O(log n)
# SC: O(1)
def findMin_binary_search(nums):
    low = 0
    high = len(nums)-1

    while low < high:
        mid = low + (high-low)//2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid+1
    
    return nums[low]
#Example usage
nums = [3,4,5,6,2]
print(findMin_binary_search(nums))  # Output: 1

# Method 3: Using built-in functions
# TC: O(n)
# SC: O(1)
def findMin_builtin(nums):
    return sorted(nums)[0]
#Example usage
nums = [4,5,6,7,0,1,2]
print(findMin_builtin(nums))  # Output: 0   