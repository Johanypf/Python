# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = ""

    for i in range(len(strs[0])):
        w = strs[0][i]

        for n in range(1, len(strs)):
          
            if i >= len(strs[n]) or strs[n][i] != w:
                return prefix
        
        prefix += w

    return prefix

strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))





