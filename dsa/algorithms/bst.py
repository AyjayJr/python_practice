class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node 
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def bfs(self):
        node = self.root
        queue = []
        results = []

        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            results.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return results


def main():
    tree = BinarySearchTree()
    tree.insert(47)
    tree.insert(21)
    tree.insert(76)
    tree.insert(18)
    tree.insert(27)
    tree.insert(52)
    tree.insert(82)
    
    print(tree.bfs())


if __name__ == "__main__":
    main()
