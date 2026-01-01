# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

#using hash map to store frequency and sorting the frequency to get top k frequent elements
#TC: O(n log n) where n is number of elements in the array
#SC : O(n) where n is number of elements in the array
# Note: Not the best solution possible
def topKFrequent(nums, k):

    #using a dictionary to store the frequency of each input
    count ={}

    for num in nums:
        count[num] = 1+ count.get(num, 0) #can't directlt use count[num] which is why we use the get function and the get function helps us initialize the count to 0 if no any previous instances of the number

    #stroing the dictionary into a sorted list
    arr = []
    for num, freq in count.items(): #.items() returns the [key, value]
        arr.append([freq, num]) #putting freq first as the sorting happens on the basis of the first index unless there's a tie
    arr.sort() #happens in ascending order

    res = [] #stores the result to return
    while len(res) < k:
        res.append(arr.pop()[1]) # pops k element from array from the last which is the largest elements and returns their 1st index
    return res

#example usage
nums = [1,1,2,2,2,3,4,4,4,4]
k = 2
print(topKFrequent(nums,k))