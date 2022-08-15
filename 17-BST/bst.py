class Node:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    
    def __repr__(self):
        return "value: " + str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.head = None
        self.step = 0

    def insert(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            current = self.head
            while current.leftChild != None or current.rightChild != None:
                if current.value > value:
                    if current.leftChild is not None:
                        current = current.leftChild
                    else:
                        current.leftChild = Node(value)
                        return
                else:
                    if current.rightChild is not None:
                        current = current.rightChild
                    else:
                        current.rightChild = Node(value)
                        return
                    
            if current.value > value:
                current.leftChild = Node(value)
            else:
                current.rightChild = Node(value)
                

    def fromArray(self, array):
        for value in array:
            self.insert(value)

    def search(self, value):
        if self.head is None: return False
        current = self.head
        self.step = 0
        while True:
            self.step += 1
            if current.value == value: return True
            if value > current.value and current.rightChild is not None:
                current = current.rightChild
            elif value < current.value and current.leftChild is not None:
                current = current.leftChild
            else: return False

    def min(self):
        current = self.head
        self.step = 0
        if current is None: return None
        while current.leftChild is not None:
            current = current.leftChild
            self.step += 1
        self.step += 1
        return current.value

    def max(self):
        current = self.head
        self.step = 0
        if current is None: return None
        while current.rightChild is not None:
            current = current.rightChild
            self.step += 1
        self.step += 1
        return current.value

    def visitedNodes(self):
        return self.step



if __name__ == '__main__':
    #bst = BinarySearchTree()
    #bst.insert(5)
    #bst.insert(3)
    #bst.insert(1)
    #bst.insert(4)
    #bst.insert(7)
    #bst.insert(6)
    #bst.insert(8)
    #bst.fromArray([5, 3, 1, 4, 7, 6, 8])
    #print(bst.min())
    #print(bst.visitedNodes())
    #print(bst.max())
    #print(bst.visitedNodes())
    #print(bst.search(9))
    #print(bst.visitedNodes())
    
    bst1 = BinarySearchTree()

    print(bst1.search(10))
    print(bst1.visitedNodes())
    print(bst1.min())
    print(bst1.max())
    
    bst2 = BinarySearchTree()
    bst2.fromArray([5, 3, 1, 4, 7, 6, 8])
    
    print(bst2.search(5))
    print(bst2.visitedNodes())
    print(bst2.search(7))
    print(bst2.visitedNodes())
    print(bst2.search(6))
    print(bst2.visitedNodes())
    print(bst2.search(10))
    print(bst2.visitedNodes())
    print("MIN: " + str(bst2.min()))
    print(bst2.visitedNodes())
    print("MAX: " + str(bst2.max()))
    print(bst2.visitedNodes())
    
    bst3 = BinarySearchTree()
    bst3.fromArray([1, 3, 4, 5, 6, 7, 8])

    print("MIN: " + str(bst3.min()))
    print(bst3.visitedNodes())
    print("MAX: " + str(bst3.max()))
    print(bst3.visitedNodes())