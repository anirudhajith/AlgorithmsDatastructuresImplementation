
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

 `BinaryTree(key, left=None, right=None)`

**Returns:**  new `BinaryTree` object

**Arguments:**
- `key`: value of key at root of new `BinaryTree`
- `left`: left subtree `BinaryTree`
- `right`: right subtree `BinaryTree`

**Time Complexity:** *ϴ(1)*

---
 `BinaryTree.createLeaf(key, direction)`

**Returns:**  `BinaryTree` corresponding to new leaf

**Usage:** creates a new leaf in direction `direction`

**Arguments:**
- `key`: value of key at new leaf
- `direction`: direction of new leaf with respect to its parent. Accepted values are `'left'` and `'right'`

**Time Complexity:** *ϴ(1)*

---
 `BinaryTree.insertSubtree(tree, direction)`

**Returns:**  `BinaryTree` corresponding to root of new subtree `tree`

**Usage:** inserts new subtree `tree` at root in direction `direction`

**Arguments:**
- `tree`: `BinaryTree` object corresponding to subtree to be inserted at root
- `direction`: direction of `tree` with respect to its parent. Accepted values are `'left'` and `'right'`

**Time Complexity:** *ϴ(1)*

---
 `BinaryTree.detachSubtree()`

**Returns:**  `BinaryTree` object which was detached from its parent

**Usage:**    detaches and returns the `BinaryTree` object

**Arguments:** None 

**Time Complexity:** *ϴ(1)*

---
 `BinaryTree.getDirection()`

**Returns:**  `'left'` or `'right'` or `None`

**Usage:** returns the direction in which the `BinaryTree` object is a child of its parent. Returns `None` if the object has no parent

**Arguments:** None

**Time Complexity:** *ϴ(1)*

---
`BinaryTree.getSize()`

**Returns:**  `int` denoting the size of the tree rooted at the `BinaryTree` object

**Usage:**  returns the size of the subtree rooted at the `BinaryTree` object

**Arguments:** None

**Time Complexity:** *ϴ(N)* where N is the size of the tree

---
`BinaryTree.getDeepCopy()`

**Returns:**  `BinaryTree` object which is a deep copy

**Usage:** constructs and returns a deep copy of the `BinaryTree` object

**Arguments:** None

**Time Complexity:** *ϴ(N)* where N is the size of the tree

---
