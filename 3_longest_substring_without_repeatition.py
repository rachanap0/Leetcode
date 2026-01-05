# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
#  Input: s = "bbabcabcbb"
# Output: 3

#sliding window approach
# TC: O(n)
# SC: O(m)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                 #example: "bbabcabcbb" when at second 'b' we need to move left pointer to right until we remove the first 'b'
                charSet.remove(s[l]) #remove the char from left 
                l +=1
            charSet.add(s[r]) #add the char from right
            longest_substring = r-l+1 #formula to calculate length of current substring
            longest = max(longest, longest_substring)
        return longest
    
#example usage
sol = Solution()
s = "bbabcabcbb"
print(sol.lengthOfLongestSubstring(s))