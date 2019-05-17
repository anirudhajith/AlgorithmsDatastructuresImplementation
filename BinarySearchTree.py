from BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def __init__(self, key):

        if key == None:
            raise ValueError('BinarySearchTree cannot have None key')
        else:
            BinaryTree.__init__(self, [key])
    
    def insert(self, key):
        currentKey = self.key[0]

        if currentKey == key:
            self.key.append(key)
        elif currentKey < key:
            if self.left == None:
                self.left = BinarySearchTree(key)
                self.left.parent = self
            else:
                self.left.insert(key)
        elif currentKey > key:
            if self.right == None:
                self.right = BinarySearchTree(key)
                self.right.parent = self
            else:
                self.right.insert(key)
        else:
            raise ValueError('Comparison failed')
    
    def delete(self):
        return self.detachSubtree()
    




'''
TODO: insert
TODO: delete
TODO: balance
TODO: find
'''