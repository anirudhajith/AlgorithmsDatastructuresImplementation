import unittest
from random import randint, random, shuffle
from Heap import Heap

class HeapTest(unittest.TestCase):
    arr1 = [randint(-100,100) for _ in range(100)]
    arr2 = [random() for _ in range(1000)]
    arr3 = arr1 + arr2
    shuffle(arr3)

    def test_init(self):
        heap1 = Heap(self.arr1)
        heap2 = Heap(self.arr2)
        #print(heap1.array)
        #print(heap2.array)
    
    def test_heap_property(self, heap = None):

        if heap == None:
            heap = Heap(self.arr3)
        
        for index in range(1, len(heap.array)):

            lIndex = heap.left(index)
            if lIndex < heap.size:
                self.assertGreaterEqual(heap.array[index], heap.array[lIndex])
            
            rIndex = heap.right(index)
            if rIndex < heap.size:
                self.assertGreaterEqual(heap.array[index], heap.array[rIndex])
            



if __name__ == '__main__':
    unittest.main()