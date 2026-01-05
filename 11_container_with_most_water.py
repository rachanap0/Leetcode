# Given an array of integers height, find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
# Input: height = [1,1]
# Output: 1         

# Brute Force approach
# TC: O(n^2)
# SC: O(1)

def maxWater(height):
    water_area = 0

    for i in range(len(height)):
        for j in range(1,len(height)):
            width = j-1
            max_height = min(height[i], height[j])
            area = width*max_height
            water_area = max(water_area, area)
    return water_area

#example usage
height = [1,7,2,5,4,7,3,6]
print(maxWater(height))

#Two Pointer Approach
# TC: O(n)
# SC: O(1)
def maxWater_pointer(height):
    l = 0
    r = len(height)-1

    water_area = 0

    while l<r:
        width = r-l
        max_height = min(height[l], height[r])
        area = width*max_height
        water_area = max(area, water_area)

        if height[l] < height[r]:
            l +=1
        else:
            r-=1
    return water_area

#example usage
height = [1,7,2,5,4,7,3,6]
print(maxWater_pointer(height))