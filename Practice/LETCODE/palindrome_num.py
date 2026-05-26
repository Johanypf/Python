# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

x = str(456)
print(x[::-1])
if x[::-1] == x:
    print(True)
