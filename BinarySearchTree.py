from BinaryTree import BinaryTree
from random import shuffle

class BinarySearchTree(BinaryTree):

    def __init__(self, array):

        shuffle(array)                                      # for random construction of BST
        
        BinaryTree.__init__(self, array[0])
        for key in array[1:]:
            self.insert(key)

    def insert(self, key):
        currentKey = self.key[0]

        if key == currentKey:
            self.key.append(key)
        elif key < currentKey:
            if self.left == None:
                self.left = type(self)(key)
                self.left.parent = self
            else:
                self.left.insert(key)
        elif key > currentKey:
            if self.right == None:
                self.right = type(self)(key)
                self.right.parent = self
            else:
                self.right.insert(key)
        else:
            raise ValueError('Comparison failed')

    def find(self, key):
        currentKey = self.key[0]

        if key == currentKey:
            return self
        elif key < currentKey:
            return (None if self.left == None else self.left.find(key))
        elif key > currentKey:
            return (None if self.right == None else self.right.find(key))
        else:
            raise ValueError('Comparison failed')

    def count(self, key):
        reference = self.find(key)
        return (0 if reference == None else return len(self.key))

    def contains(self, key):
        count = self.count(key)
        return (True if count > 0 else False)

    def delete(self, key):
        reference = self.find(key)

        if reference == None:
            return False
        else:
            reference._delete()
            return True

    def rotate(self, direction):
        pass
    
    def getMinimum(self):
        return (self.key[0] if self.left == None else self.left.getMinimum())
    
    def getMaximum(self):
        return (self.key[0] if self.right == None else return self.right.getMaximum())
    
    def getSuccessor(self):
        direction = self.getDirection()
        if direction == 'right' or direction == None:
            if self.right == None:
                return None
            else:
                return self.right.getMinimum()
        elif direction == 'left':
            if self.right == None:
                return self.parent
            else:
                return self.right.getMinimum()


    def _delete(self):

        if len(self.key) > 1:
            self.key.pop()
        else:
            direction = self.getDirection()

            if direction == None:
                pass
            else:
                if direction == 'left':
                    if self.left == None and self.right == None:
                        self.parent.left = None
                        self.parent = None
                    elif self.left == None:
                        self.right.parent = self.parent
                        self.parent.left = self.right
                        self.parent = None
                        self.right = None
                    elif self.right == None:
                        self.left.parent = self.parent
                        self.parent.left = self.left
                        self.parent = None
                        self.left = None
                    else:
                        pass




                elif direction == 'right':
                    if self.left == None and self.right == None:
                        self.parent.right = None
                        self.parent = None
                    elif self.left == None:
                        self.right.parent = self.parent
                        self.parent.right = self.right
                        self.parent = None
                        self.right = None
                    elif self.right == None:
                        self.left.parent = self.parent
                        self.parent.right = self.left
                        self.parent = None
                        self.left = None
                    else:
                        pass


'''
Required Functionality:

__init__(array): returns binary search tree initialized with an array of elements
find(key): returns node containing key
count(key): returns count of key in BST
contains(key): Checks if BST contains key
findSuccessor(key): returns successor node
findPredecessor(key): returns predecessor node
getSuccessor(key): returns successor node key
getPredecessor(key): returns predecessor node key
rotate(node): rotates
insert(key): inserts key into BST
delete(key): deletes key from BST
getMinimum(): returns value of smallest key in tree
getMaximum(): returns value of largest key in tree
findMinimum(): returns reference to node containing smallest value in tree
findMinimum(): returns reference to node containing largest value in tree

'''
