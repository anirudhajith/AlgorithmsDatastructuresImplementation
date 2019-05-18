from BinaryTree import BinaryTree

class BinarySearchTree(BinaryTree):
    
    def __init__(self, key):

        if key == None:
            raise ValueError(self.__class__.__name__ + ' cannot have None key')
        else:
            BinaryTree.__init__(self, [key])
    
    def insert(self, key):
        currentKey = self.key[0]

        if ckey == currentKey:
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
            if self.left == None:
                return False
            else:
                return self.left.find(key)
        elif key > currentKey:
            if self.right == None:
                return False
            else:
                return self.right.find(key)
        else:
            raise ValueError('Comparison failed')
    
    def count(self, key):
        reference = self.find(key)
        if reference == False:
            return 0
        else:
            return len(self.key)
    
    def contains(self, key):
        count = self.count(key)

        if count > 0:
            return True
        else:
            return False
    
    def delete(self, key):
        reference = self.find(key)

        if reference == False:
            return False
        else:
            reference._delete()
            return True            
    
    def _delete(self):

        if len(self.key) > 1:
            self.key.pop()
        else:
            direction = self.getDirection()
            if direction == 'left' and self.right == None:
                self.left.parent = self.parent
                self.parent.left = self.left
                self.parent = None
                self.left = None
            elif direction == 'right' and self.left == None:
                self.right.parent = self.parent
                self.parent.right = self.right
                self.parent = None
                self.right = None
            elif direction == None:
                if self.right == None:
                    self.left.parent = None
                    self.parent = None
                    self.left = None
                elif self.left == None:
                    self.right.parent = None
                    self.parent = None
                    self.right = None

        
    




'''
TODO: insert DONE
TODO: delete DONE
TODO: balance
TODO: find DONE
'''