class Heap:
    def __init__(self, array):

        self.array = [None]
        self.array.extend(array)
        self.size = len(array)

        self.buildMaxHeap()

    def maxHeapify(self, index):
        largestIndex = index

        if self.left(index) <= self.size:
            if self.array[self.left(index)] > self.array[largestIndex]:
                largestIndex = self.left(index)

        if self.right(index) <= self.size:
            if self.array[self.right(index)] > self.array[largestIndex]:
                largestIndex = self.right(index)

        if largestIndex != index:
            self.swap(largestIndex, index)
            self.maxHeapify(largestIndex)

    def buildMaxHeap(self):
        for index in range(self.size // 2, 0, -1):
            self.maxHeapify(index)

    def increaseKey(self, index, key):
        if key <= self.array[index]:
            raise ValueError(
                'increaseKey failed: key ' + str(key) + ' is too small'
            )
        else:
            self.array[index] = key
            while self.parent(index) >= 1 and self.array[self.parent(index)] < self.array[index]:
                self.swap(index, self.parent(index))
                index = self.parent(index)

    def getMax(self):
        return self.array[1]

    def extractMax(self):
        if self.size > 0:
            self.swap(1, self.size)
            self.array.pop()
            self.size -= 1
            self.maxHeapify(1)
        else:
            raise LookupError(
                'extractMax failed: heap is empty'
            )

    def insert(self, key):
        self.array.append(key)
        self.size += 1

        index = self.size
        while self.parent(index) >= 1 and self.array[self.parent(index)] < self.array[index]:
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def sort(self):
        fullSize = self.size
        sortedArray = []
        for index in range(fullSize):
            sortedArray.append(self.getMax())
            self.extractMax()
        
        sortedArray.reverse()
        return sortedArray
        

    def left(self, index):
        return index * 2

    def right(self, index):
        return (index * 2) + 1

    def parent(self, index):
        return index // 2

    def swap(self, index1, index2):
        temp = self.array[index1]
        self.array[index1] = self.array[index2]
        self.array[index2] = temp


A = [3, 8, 2 , 9, -1, 0, 6, 9, 22, 7, -5, 8, 9.2, 3.14, 10, 9, -3, 5, 8, 2.73, 12, 8]
aHeap = Heap(A)
print(aHeap.array)
aHeap.insert(17)
print(aHeap.array)
aHeap.extractMax()
print(aHeap.array)

print(aHeap.sort())
print(aHeap.array)