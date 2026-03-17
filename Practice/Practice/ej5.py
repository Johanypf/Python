find_famous_cat1 =[
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
]


def find_famous_cat(cats):
    new_list= []
    mayor_actual = 0
    for x in cats:
        x_suma = sum(x["followers"])
        if mayor_actual is None or x_suma > mayor_actual:
            mayor_actual = x_suma
            new_list = [x["name"]]
        elif x_suma == mayor_actual:
            new_list.append(x["name"])          
    return new_list


print(find_famous_cat(find_famous_cat1))




