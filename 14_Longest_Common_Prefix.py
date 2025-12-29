# Longest prefix problem means to find the longest common starting substring among a list of strings.
# eg Given str = ['Flower', 'flow', 'flood'], then the longest common prefix will be flo
# if only first character common return only the first char else returns empty string ''

# here sorting takes n(nlogn . m) time where n is number of strings and m is average length of string
# then comparing first and last string takes O(m) time
# total time complexity is O(nlogn . m)    

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not str:
            return ""
        
        res = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]
        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                res += first[i]
            else:
                break
        return res
    
# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))  # Output: "fl"
print(solution.longestCommonPrefix(["dog","racecar","car"]))   # Output: ""