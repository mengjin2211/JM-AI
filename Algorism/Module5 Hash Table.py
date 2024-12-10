class HashTableChaining:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
    def display(self):
        print("Hash Table (Chaining Visualization):")
        for i, chain in enumerate(self.table):
            if chain !=[]:
                print(f"Index {i}: {chain}")

def ContentRecommendation(userid, userTable, contentTable):    
    if not userTable.get(userid):
        return []

    user_interests = userTable.get(userid) 
    recommended_content = [] 
    for index in range(contentTable.size):
        for content_id, content_tags in contentTable.table[index]:
            if any(tag in user_interests for tag in content_tags):
                recommended_content.append((content_id, content_tags))
    return recommended_content

def main():

    user_table=HashTableChaining(50)
    content_table=HashTableChaining(100)

    user_table.insert("user_1", ["tech", "music", "AI"])
    user_table.insert("user_2", ["fashion", "travel", "food"])
    user_table.insert("user_3", ["sports", "tech", "news"])

    content_table.insert("content_1", ["tech", "AI", "innovation"])
    content_table.insert("content_2", ["food", "cooking", "travel"])
    content_table.insert("content_3", ["sports", "fitness", "health"])
    content_table.insert("content_4", ["music", "entertainment", "pop"])
    
    print('User Table:')
    user_table.display()
    print('Content Table:')
    content_table.display()
    
    user_id=["user_1","user_2","user_3"]
    for i in user_id:
        recommendations = ContentRecommendation(i, user_table, content_table)
        print(f"Recommendations for {i}: {recommendations}")

if __name__ == "__main__":
    main()

