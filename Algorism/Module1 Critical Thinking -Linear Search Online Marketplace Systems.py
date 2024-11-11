#Linear Search Online Marketplace Systems 
#In real-world scenario, I would first build connection with the sql database using APIs and query the items to build items list. 

items = [
    {'id': 1, 'item_name': 'hand warmer', 'price': 28.5, 'category': 'electronics', 'description': 'keep your hands warm in winter'},
    {'id': 2, 'item_name': 'long johns', 'price': 15, 'category': 'clothing', 'description': 'cotton'},
    {'id': 3, 'item_name': 'chair', 'price': 60, 'category': 'furniture', 'description': 'good quality'},]

def search_criteria(item=None, Price=None, Category=None, Desc=None):   
    search={'item_name': item, 'price': Price, 'category': Category, 'description':Desc}
    return {key: value for key, value in search.items() if value is not None}


def linear_search (items, search):
    match=[]
    partial_match=[]
    searchKey = {key: value for key, value in search.items() if value is not None and value != ''}

    for item in items:
        match_count = 0
        for key, value in searchKey.items():  
            match_count = sum(1 for key, value in searchKey.items() if key in item and item[key] == value)

        if match_count == len(searchKey):
            match.append(item)
        elif 0<match_count < len(searchKey):
            partial_match.append(item)             
    return match, partial_match
def print_items(search, match, partial_match):
    print(f'for search criteria {search}','\n'
        f'{len(match)} perfect match: {match}\n{len(partial_match)} partial match:{partial_match}')

search1 = search_criteria(item='hand warmer', Category='electronics')
match, partial_match = linear_search(items, search1)
print_items(search1,match, partial_match)
search2 = search_criteria(item='chair', Price=20)
match, partial_match = linear_search(items, search2)
print_items(search2, match, partial_match)
 