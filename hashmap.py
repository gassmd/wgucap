class HashMap:
    # Our HashMap Constructor that includes various methods
    # Space-time complexity O(1)
    def __init__(self, initial_capacity):
        # initializes hashtable
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # magic method to get size of hashmap for iterating purposes O(n)
    def __sizeof__(self):
        return len(self.map)

    # gets hash key, O(1)
    def get_hash_key(self, key):
        return int(key) % len(self.map)

    # adds value to table, O(1)
    def add(self, key, value):
        key_hash = self.get_hash_key(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # updates value at key location, O(N)
    def update(self, key, value):
        key_hash = self.get_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
        else:
            print('Error updating on key: ' + key)
            return False

    # get value at key location, O(N)
    def get(self, key):
        key_hash = self.get_hash_key(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # deletes value from hash table, O(N)
    def delete(self, key):
        key_hash = self.get_hash_key(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


    # deletes every value from the table, O(n)
    def clear(self):
        for i in range(0, len(self.map)):
            self.delete(i)

    def search(self, search_term):
        search_result = []
        for i in range(0, len(self.map)):
            key_hash = i
            result = self.get(key_hash)
            if search_term in str(result):
                search_result.append(result)
        if len(search_result) == 0:
            print('no search values found')
        return search_result

    def contains(self, contains_search):
        query = self.search(contains_search)
        if len(query)>0:
            return False

    def print_map(self):
        for i in range(0, len(self.map)):
            key_hash = i
            if self.get(key_hash) is not None:
                team_name = str(self.get(key_hash).name)
                print('KEY: ' + str(key_hash) + ' | VALUE: ' + str(self.get(key_hash)))
                print(team_name)
                print('-------------')

class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
