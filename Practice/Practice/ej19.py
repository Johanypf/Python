# Input:
# count_words_by_length([
#   "apple",
#   "banana",
#   "orange",
#   "grapefruit",
#   "pear",
#   "kiwi"
# ])

# Output:
# {5: 1, 6: 2, 10: 1, 4: 2}



def count_words_by_length(words):
  new_dic = {}
  for letter in words:
        if len(letter) in new_dic:
            new_dic[len(letter)] += 1
        else:
            new_dic[len(letter)] = 1

  return new_dic