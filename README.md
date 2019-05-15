# Implementations of some Algorithms and Datastructures in Python

## Heap
#### Implemented in `Heap.py`

| Function | Description | Time Complexity |
|----------|-------------|------------------|
|`Heap(array)`| returns a `Heap` object initialized to contain the same elements as `array` | *ϴ(n)* |
| `getMax()` | returns the largest element in the `Heap` object | *ϴ(1)* |
| `extractMax()` | removes the largest element in the `Heap` object | *ϴ(log n)* |
| `insert(key)` | inserts key into the `Heap` object | *ϴ(log n)* |
| `increaseKey(index, key)` | increases the value of the element at the position `index` in the `Heap` object to `value` | *ϴ(log n)* |
| `sort()` | returns a list of the `Heap` elements in sorted order | *ϴ(n log n)* | 


## BinaryTree 
#### Implemented in:  `BinaryTree.py`

 ### `BinaryTree(node=None)`

**returns:**  `BinaryTree` object

**Usage:** 
- `BinaryTree()` returns an empty `BinaryTree`
- `BinaryTree(node)` returns a `BinaryTree` object whose root is initialized to the `Node` object `node`

**Time Complexity:** *ϴ(1)*

---
 ### `BinaryTree.createLeaf(key, parentNode=None, direction=None)`

**returns:**  `Node` object

**Usage:** 
- `BinaryTree.createLeaf(key)` is used to initialize an empty `BinaryTree` with a single `Node` of key `key`. A reference to this `Node` object is returned. 
- `BinaryTree.createLeaf(key, parentNode, direction)` is used to create a new leaf at `parentNode` in direction `direction`

**Time Complexity:** *ϴ(1)*

---
 ### `BinaryTree.insertSubtree(tree, parentNode=None, direction=None)`

**returns:**  void

**Usage:** 
- `BinaryTree.insertSubtree(tree)` is used to initialize an empty `BinaryTree` to `tree`
- `BinaryTree.insertSubtree(tree, parentNode, direction)` inserts `tree` at `parentNode` in direction `direction`

**Time Complexity:** *ϴ(1)*

---
 ### `BinaryTree.detachSubtree(root)`

**returns:**  `BinaryTree` object

**Usage:** 
- `BinaryTree.detachSubtree(root)` detaches and returns the `BinaryTree` rooted at `root` 

**Time Complexity:** *ϴ(1)*

---
 ### `BinaryTree.getChildDirection(node)`

**returns:**  `string` or `None`

**Usage:** 
- `BinaryTree.getChildDirection(node)` returns `'left'` or `'right'` denoting the direction in which `node` is a child of `node.parent`
- `BinaryTree.getChildDirection(tree.root)` returns `None`

**Time Complexity:** *ϴ(1)*

---
### `BinaryTree.getSubtreeSize(root)`

**returns:**  `int`

**Usage:** 
- `BinaryTree.getSubtreeSize(root)` returns the size of the subtree rooted at `root`

**Time Complexity:** *ϴ(N)*

---
### `BinaryTree.getDeepCopyNode(root)`

**returns:**  `Node` object

**Usage:** 
- `BinaryTree.getDeepCopyNode(root)` returns a deep copy of the `Node` object which represents the root of the subtree rooted at `root`

**Time Complexity:** *ϴ(h)*

---
### `BinaryTree.getDeepCopySubtree(root)`

**returns:**  `BinaryTree` object

**Usage:** 
- `BinaryTree.getDeepCopySubtree(root)` returns a `BinaryTree` object which represents deep copy of the  subtree rooted at `root`

**Time Complexity:** *ϴ(h)*

---

