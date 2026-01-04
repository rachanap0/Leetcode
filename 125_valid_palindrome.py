# Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.     

# Reverse String
# TC: O(n)
#SC: O(n)
def isPalindrome(s):
    newStr = ''
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

#example usage
s = "tab a cat"
print(isPalindrome(s))

# #Using two pointer.
#TC: O(n)
#SC: O(1)

class Solution:
    def isPalindrome_pointer(self, s):
        left = 0
        right = len(s)-1

        while left <right:
            while left<right and not self.alphanum(s[left]):
                left +=1
            while right > left and not self.alphanum(s[right]):
                right -=1
            if s[left].lower() != s[right].lower():
                return False
            left +=1
            right -=1
        return True

    def alphanum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

#example usage
sol = Solution()
s2 ="Was it a car or a cat I saw?"
print(sol.isPalindrome_pointer(s2))