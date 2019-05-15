class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinaryTree:
    def __init__(self, node=None):
        self.root = node
        self.size = self.getSubtreeSize(node)

    def createLeaf(self, key, parentNode=None, direction=None):

        node = Node(key)

        if parentNode == None:
            if self.root == None:
                self.root = Node(key)
            else:
                raise ValueError('Invalid parentNode: BinaryTree is not empty')
        else:
            if direction == 'left':
                if parentNode.left == None:
                    parentNode.left = node
                    node.parent = parentNode
                else:
                    raise ReferenceError('parentNode.left is not None')

            elif direction == 'right':
                if parentNode.right == None:
                    parentNode.right = node
                    node.parent = parentNode
                else:
                    raise ReferenceError('parentNode.right is not None')

            else:
                raise ValueError('Invalid direction')

        self.size += 1
        return node

    def insertSubtree(self, tree, parentNode=None, direction=None):
        if parentNode == None:
            if self.root == None:
                self.root = tree.root
            else:
                raise ValueError('Invalid parentNode: BinaryTree is not empty')
        else:
            if direction == 'left':
                if parentNode.left == None:
                    parentNode.left = tree.root
                    tree.root.parent = parentNode
                else:
                    raise ReferenceError('parentNode.left is not None')

            elif direction == 'right':
                if parentNode.right == None:
                    parentNode.right = tree.root
                    tree.root.parent = parentNode
                else:
                    raise ReferenceError('parentNode.right is not None')

            else:
                raise ValueError('Invalid direction')

        self.size += tree.size

    def detachSubtree(self, root):
        direction = self.getChildDirection(root)

        if direction == 'left':
            root.parent.left = None
        elif direction == 'right':
            root.parent.right = None
        else:
            self.root = None

        root.parent = None
        self.size -= self.getSubtreeSize(root)
        
        return BinaryTree(root)

    def getChildDirection(self, node):
        parent = node.parent
        if parent != None:
            if parent.left == node:
                return 'left'
            elif parent.right == node:
                return 'right'
        else:
            return None
    
    def getSubtreeSize(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.getSubtreeSize(root.left) + self.getSubtreeSize(root.right)
    
    def getDeepCopyNode(self, root):
        copyRoot = Node(root.key)

        if root.left != None:
            copyRoot.left = self.getDeepCopySubtree(root.left)
        if copyRoot.right != None:
            copyRoot.right = self.getDeepCopySubtree(root.right)
        
        return copyRoot

    def getDeepCopySubtree(self, root):
        return BinaryTree(self.getDeepCopyNode(root))
