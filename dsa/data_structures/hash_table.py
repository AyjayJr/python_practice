class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item
        return None

    def get_keys(self):
        ret = []
        for index in self.data_map:
            if index is not None:
                for item in index:
                    ret.append(item[0])
        return ret

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(f'{i}:{val}')


def main():
    ht = HashTable()
    ht.print_table()
    print()
    ht.set_item('bolts', 1400)
    ht.set_item('washers', 50)
    ht.set_item('lumber', 70)
    ht.print_table()
    item = ht.get_item('bolts')
    print(item)
    print(ht.get_keys())

if __name__ == "__main__":
    main()  
