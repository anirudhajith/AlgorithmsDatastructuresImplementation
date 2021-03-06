class BinaryTree:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.parent = None

        if (not isinstance(left, type(self)) and left != None) or (not isinstance(right, type(self)) and right != None):
            raise ValueError('Children must be instances of ' + self.__class__.__name__)
        if key == None:
            raise ValueError(self.__class__.__name__ + ' cannot have None key')
        else:
            if left != None:
                left.parent = self
            if right != None:
                right.parent = self

    def createLeaf(self, key, direction):
        return self.insertSubtree(type(self)(key), direction)

    def insertSubtree(self, tree, direction):
        if not isinstance(tree, type(self)):
            raise ValueError('tree is not an instance of ' + self.__class__.__name__)
        else:
            if direction == 'left':
                self.left = tree
            elif direction == 'right':
                self.right = tree
            else:
                raise ValueError('Invalid direction')

            tree.parent = self
            return tree

    def detachSubtree(self):
        direction = self.getDirection()

        if direction == 'left':
            self.parent.left = None
        elif direction == 'right':
            self.parent.right = None

        self.parent = None
        return self

    def getDirection(self):
        parent = self.parent
        if parent != None:
            if parent.left is self:
                return 'left'
            elif parent.right is self:
                return 'right'
        else:
            return None

    def getSize(self):
        size = 1

        if self.left != None:
            size += self.left.getSize()
        if self.right != None:
            size += self.right.getSize()

        return size

    def getDeepCopy(self):
        copy = type(self)(self.key)

        if self.left != None:
            copy.left = self.left.getDeepCopy()
        if self.right != None:
            copy.right = self.right.getDeepCopy()

        return copy
