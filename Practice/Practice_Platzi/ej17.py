sets = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

# find_set_intersection(sets)


# a = {2, 3, 4, 5}
# b = {3, 4, 5, 6}
# # Output: {3, 4}
# intersection_1 = a.intersection(b)
intersection_2 =  sets[0]
# print(intersection_1)

for i in sets[1:]:
    intersection_2 &= i

print(intersection_2)



def find_set_intersection(sets):
  # Tu código aquí 👈
  if not sets:
    return set()
  intersection_2 =  sets[0]


  for i in sets[1:]:
    intersection_2 &= i

  return intersection_2
    

