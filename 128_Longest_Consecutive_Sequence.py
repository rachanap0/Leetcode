# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#method: Hash Set
# TC: O(n)
# SC: O(n)
def longestConsecutiveSequence(nums):
    numSet = set(nums)
    #keep a counter to track the count of the largest sequence
    longest = 0

    #for every number check if its previous number exists in the set
    for num in nums:
        if(num-1) not in numSet:
            length =1 # at least the number itself is there
            while(num+length) in numSet: #loop to check for the next consecutive numbers
                length +=1
            longest = max(length, longest) #update the longest sequence if found a longer one
    return longest


#example usage
nums = [2,20,4,10,3,4,5]
print(longestConsecutiveSequence(nums))