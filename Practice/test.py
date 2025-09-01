word = {'m': 1, 'a': 3, 'n': 2, 'z': 1}
rep = []
for x,y in word.items():
    if y > 1:
        rep.append(x)


print(rep)