# Input: "Hola mundo"

# Output: {
#   'H': 1, 
#   'o': 2, 
#   'l': 1, 
#   'a': 1, 
#   ' ': 1, 
#   'M': 1, 
#   'u': 1, 
#   'n': 1, 
#   'd': 1
# }


def count_letters(phrase):
  # Tu código aquí 👈
    count= {}

    for letter in phrase:
        if not letter in count:
            count[letter] = 1
        else:
            count[letter] += 1 


    return count
  