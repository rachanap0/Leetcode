# Given a string s and an integer k, you can choose any character of the string and change it to any other uppercase English character at most k times.
# Find the length of the longest substring containing the same letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:
# Input: s = "AABABBA", k = 1               

#sliding window approach
def longestrepeating(s, k):
    l = 0
    res = 0
    count = {}
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf , count[s[r]])

        while (r-l+1) - maxf > k:
            count[s[l]] -=1 
            l +=1
        res = max(res, r-l+1)
  
    return res

#example usage
s = "ABABBA"
k =2
print(longestrepeating(s, k))