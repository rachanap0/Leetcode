# Valid Anagram 
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

#hash map approach
class Solution(object):
    def isAnagram(self, s, t ):
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]]= 1 + countT.get(t[i], 0)
        return countS == countT
    
solution = Solution()
s = 'racecar'
t = 'raccear'
print(solution.isAnagram(s,t))

#hashTable approach using array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = [0] *26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] +=1
            count[ord(t[i]) - ord('a')] -=1
        
        for val in count:
            if val != 0:
                return False
        return True
    
#example usage
solution = Solution()
s = "toys"
t = "ysot"
print(solution.isAnagram(s,t))