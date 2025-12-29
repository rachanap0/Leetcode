# Given a binary array nums, return the maximum number of consecutive 1's in the array.
def max_ones(num):
    count = 0
    max_count = 0

    for i in num:
        if i == 1:
            count +=1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)

arr = [1,1,2,3,1,1,1]
print(max_ones(arr))