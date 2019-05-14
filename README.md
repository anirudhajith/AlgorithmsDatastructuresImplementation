# Implementations of some Algorithms and Datastructures in Python

### Heap
##### Implemented in `Heap.py`

| Function | Description | Time Complexity |
|----------|-------------|------------------|
|`Heap(array)`| returns a `Heap` object initialized to contain the same elements as `array` | *ϴ(n)* |
| `getMax()` | returns the largest element in the `Heap` object | *ϴ(1)* |
| `extractMax()` | removes the largest element in the `Heap` object | *ϴ(log n)* |
| `insert(key)` | inserts key into the `Heap` object | *ϴ(log n)* |
| `increaseKey(index, key)` | increases the value of the element at the position `index` in the `Heap` object to `value` | *ϴ(log n)* |
