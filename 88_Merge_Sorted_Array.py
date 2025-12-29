#You are given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    #edge case of empty num2 would mean no changes to nums1
    if not nums2:
        return nums1

    #starting from the last i.e. the largest value
    i = m-1 #pointing last value of nums1 (index is 1 value less than length)
    j = n-1 #pointing to the last value of nums2 (index is 1 value less than length)
    k = m+n -1 #pointing to the last value of the merged array which is m+n but 1 value less than length

    while i>=0 and j>=0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -=1 #decrease the pointer
        else:
            nums1[k] = nums2[j]
            j -=1 #decrease the j pointer
        k -=1 #no matter which one was the largest we decrease the k pointer

    #if there are remaining elements in nums2
    while j>=0:
        nums1[k] = nums2[j]
        j -=1
        k -=1
    return nums1

#Example usage:
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
n = 3
m = 3
print(merge(nums1,m,nums2,n))