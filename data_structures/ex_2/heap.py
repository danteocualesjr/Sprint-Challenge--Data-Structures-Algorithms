def heapsort(arr):
  heap = Heap()
  sorted_list = []
  for item in arr:
    heap.insert(item)
  while heap.size > 0:
    sorted_list.insert(0, heap.delete())
  return sorted_list

# def swap(arr, i, j):
#   arr[i], arr[j] = arr[j], arr[i]

# def is_heap(arr):
#   n = 0
#   m = 0
#   while True:
#     for i in [0, 1]:
#       m += 1
#       if m > len(a):
#         return True
#       if a[m] > a[n]:
#         return False
#     n += 1

# def sift_down(arr, n, max):
#   while True:
#     biggest = n
#     c1 = 2 * n + 1
#     c2 = c1 + 1
#     for c in [c1, c2]:
#       if c < max and arr[c] > a[biggest]:
#         biggest = c
#       if biggest == n:
#         return
#       swap(a, n, biggest)
#       n = biggest

# def heapify(arr):
#   i = len(arr) / 2 - 1
#   max = len(arr)
#   while i >= 0:
#     sift_down(arr, i, max)
#     i -= 1

# def heapsort(arr):
#   heapify(arr)
#   j = len(arr) - 1
#   while j > 0:
#     swap(arr, 0, j)
#     j -= 1

class Heap:
  def __init__(self):
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    retval = self.storage[1]
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    self.storage.pop()
    self._sift_down(1)
    return retval 

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        self.storage[index], self.storage[index // 2] = self.storage[index // 2], self.storage[index]
      index = index // 2

  def _sift_down(self, index):
    while (index * 2) <= self.size:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1