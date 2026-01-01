# given an array of strings, group anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.    
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]   

from collections import defaultdict
def groupAnagram(strs):
    dict = defaultdict(list)

    for word in strs:
        count = [0] *26
        for char in word:
            count[ord(char) - ord('a')] +=1
        dict[tuple(count)].append(word)
    return list(dict.values())

#example usage
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(groupAnagram(strs))