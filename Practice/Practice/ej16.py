# Input: find_largest_palindrome(["racecar", "level", "world", "hello"])

# Output: "racecar"

words = ["Platzi", "Python", "django", "flask"]


def find_largest_palindrome(words):
  # Tu código aquí 👈
    new_word = []
    longest_word = None
    for word in words:
        inver_word = word[::-1]
        if  inver_word == word:
            new_word.append(inver_word)
        

            if len(new_word) == 0:
                new_word = None
    cant = 0
    for long in new_word:
        if len(long) > cant:
            cant = len(long)
        
            longest_word = long
        

    

    return longest_word

print(find_largest_palindrome(words))

        