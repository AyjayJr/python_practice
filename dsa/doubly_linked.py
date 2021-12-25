class Node:
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0: 
            return None

        temp = self.tail
        self.tail = temp.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next 
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        next = self.get(index)
        prev = temp.prev

        new_node.prev = prev
        new_node.next = next 
        prev.next = new_node
        next.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        next = temp.next
        prev = temp.prev

        next.prev = prev
        prev.next = next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


def main():
    double = DoublyLinkedList(0)
    double.append(1)
    double.append(2)
    double.append(3)
    double.append(4)
    double.append(5)
    double.print_list()
    print()
    print(double.get(2))
    print(double.get(5)) 

if __name__ == "__main__":
    main()
