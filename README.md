

# Implementations of some Algorithms and Datastructures in Python

## Heap
#### Implemented in `Heap.py`
`Heap(array)`

**Returns:** a new `Heap` object initialized to contain the same elements as `array` 

**Usage:** returns a `Heap` object populated with the elements of `array`

**Arguments:** 
- `array`: a list containing the elements the `Heap` object has to be initialized with

**Time Complexity:** *ϴ(N)* where N = `len(array)` 

---
`Heap.getMax()`

**Returns:** the largest element in the `Heap` object

**Arguments:** None

**Usage:** returns the largest element in the `Heap` without disturbing the `Heap` object

**Time Complexity:** *ϴ(1)*

---
`Heap.extractMax()`

**Returns:** None

**Arguments:** None

**Usage:** removes the largest element in the `Heap` object

**Time Complexity:** *ϴ(h)* where h is the height of the `Heap` object

---
`Heap.insert(key)`

**Returns:** None

**Arguments:**
- `key`: element to be inserted into the `Heap` object

**Usage:** inserts `key` into the `Heap` object

**Time Complexity:** *ϴ(h)* where h is the height of the `Heap` object

---
`Heap.increaseKey(index, key)`

**Returns:** None

**Arguments:**
- `index`: `int` index of element to be increased
- `key`: new value of element

**Usage:** increases the element at position `index` to value `key`

**Time Complexity:** *ϴ(h)* where h is the height of the `Heap` object

---
`Heap.sort()`

**Returns:** sorted list of elements in `Heap` object

**Arguments:** None

**Usage:** returns a sorted list of elements in `Heap` object. `Heap` object is rendered empty after the call.

**Time Complexity:** *ϴ(N log N)* where N is the number of elements in the `Heap`

---
## BinaryTree 
#### Implemented in:  `BinaryTree.py`

 `BinaryTree(key, left=None, right=None)`

**Returns:**  new `BinaryTree` object

**Usage:** returns a `BinaryTree` object whose root key is `key`, left pointer points to `left` and right pointer points to `right`

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
