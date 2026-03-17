import math


def vel_en_caida_libre(altura:float)->float:
    vf = math.sqrt((2*9.8*altura))
    return round(vf,2)


print(vel_en_caida_libre(5.3))