items = [
    {'id': 1, 'item_name': 'hand warmer', 'price': 28.5, 'category': 'electronics', 'description': 'keep your hands warm in winter'},
    {'id': 2, 'item_name': 'long johns', 'price': 15, 'category': 'clothing', 'description': 'cotton'},
    {'id': 3, 'item_name': 'chair', 'price': 60, 'category': 'furniture', 'description': 'good quality'},
]

def search_criteria(item=None, Price=None, Category=None, Desc=''):
    search = {'item_name': item, 'price': Price, 'category': Category, 'description': Desc}
    return {key: value for key, value in search.items() if value is not None}

def linear_search(items, search):
    match = []
    partial_match = []
    searchKey = {key: value for key, value in search.items() if value is not None}

    print(f"Search criteria: {searchKey}")

    for item in items:
        match_count = 0
        for key, value in searchKey.items():
            if key in item and item[key] == value:
                match_count += 1

        print(f"Item: {item}, Match count: {match_count}")

        if match_count == len(searchKey):
            match.append(item)
        elif 0 < match_count < len(searchKey):
            partial_match.append(item)

    return match, partial_match

# Example usage
search1 = search_criteria(item='hand warmer', Category='electronics')
match, partial_match = linear_search(items, search1)

# Calculate the number of perfect matches
match_count = len(match)

print(f'{match_count} perfect match: {match}\npartial match: {partial_match}')
