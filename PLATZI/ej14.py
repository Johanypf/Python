

def get_packages_info(packages):
   # Tu código aquí 👈
    weidght = 0
    destinations = {}
    new_dict = {} 
    for data  in packages:
        weidght += data[1]
        if not data[2] in destinations:
            destinations[data[2]] = 1
        else:
            destinations[data[2]] += 1 

    new_dict = { "total_weight": round(weidght,2),
                "destinations" : destinations
            }


    return new_dict



