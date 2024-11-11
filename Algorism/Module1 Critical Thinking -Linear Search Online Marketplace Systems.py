"""Linear Search Online Marketplace Systems 
    1) Simulate connection to postgres database using retrieve_data(), existing with a manually created items list.
    2) define_criteria() gives user flexibility to choose customized keywords to search the marketplace. If no keyword is provided, then default None.
    3) linear_search() searches through all items in the marketplace for perfect match or partial match, appending results to two arrays.
    4) print_items() prints the search result.
"""

#import psycopg2
def retrieve_data():
    conn_params = None
    try:
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()
        cursor.execute("SELECT item_name, price, category, description FROM marketplace_items")
        item_rows = cursor.fetchall()
        items = [
            {   'item_name': row[0],
                'price': row[1],
                'category': row[2],
                'description': row[3]
            }
            for row in item_rows
        ]       
        return items   
    except Exception as e:
        print("Error connecting to the database. Create your own data instead")
        items = [
        {'item_name': 'hand warmer', 'price': 28.5, 'category': 'electronics', 'description': 'keep your hands warm in winter'},
        {'item_name': 'long johns', 'price': 15, 'category': 'clothing', 'description': 'cotton'},
        {'item_name': 'chair', 'price': 60, 'category': 'furniture', 'description': 'good quality'},]
        return items
    finally:
        try:
            cursor.close()
            connection.close()
        except:
            pass

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
    print(f'for search criteria {search.values()}','\n'
        f'{len(match)} perfect match: {match}\n{len(partial_match)} partial match:{partial_match}')

items=retrieve_data()
search1 = search_criteria(item='hand warmer', Category='electronics')
match, partial_match = linear_search(items, search1)
print_items(search1,match, partial_match)
search2 = search_criteria(item='chair', Price=20)
match, partial_match = linear_search(items, search2)
print_items(search2, match, partial_match)
 