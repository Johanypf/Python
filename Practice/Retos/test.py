full_dataset= [
{'name': 'Peach', 'items': ['green shell', 'banana', 'green shell'], 'finish': 3},
{'name': 'Peach', 'items': ['green shell', 'banana', 'green shell'], 'finish': 1}, 
{'name': 'Bowser', 'items': ['green shell'], 'finish': 1},
{'name': None, 'items': ['green shell'], 'finish': 2}, 
{'name': 'Bowser', 'items': ['green shell'], 'finish': 1}, 
{'name': None, 'items': ['red shell'], 'finish': 1}, 
{'name': 'Yoshi', 'items': ['banana', 'blue shell', 'banana'], 'finish': 7}, 
{'name': 'DK', 'items': ['blue shell', 'star'], 'finish': 1}
]


def best_items(racers):
    winner_item_counts = {}
    count_none = 0
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for i in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if i not in winner_item_counts:
                    winner_item_counts[i] = 0
                winner_item_counts[i] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
                
        if racer['name'] is None:
            count_none +=1


    
    print(f"WARNING: Encountered racer with unknown name on iteration {(len(racers))-(count_none)}/{len(racers)} (racer = None)")
    return winner_item_counts


best_items(full_dataset)