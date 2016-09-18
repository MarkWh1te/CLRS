# coding:utf-8
from heap_sort import max_heapify, parent


def heap_maximum(A):
    return A[0]


def heap_extract_max(A):
    heapsize = len(A) - 1
    if heapsize < 2:
        raise Exception('heap underflow')
    max = A[0]
    A[0] = A[heapsize]
    heapsize -= 1
    A.pop()
    max_heapify(A, heapsize, 0)
    return max
#  a = [15,13,9,5,12,8,7,4,0,6,2,1]
#  print(a)
#  print(heap_extract_max(a))
#  print(a)

def heap_increase_key(A, i, key):
    if key < A[i]:
        raise Exception('key is small than current key')
    A[i] = key
    while i > 1 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def max_heap_insert(A, key):
    heapsize = (len(A) - 1) + 1
    A.append(0)
    A[heapsize] = key - 1
    heap_increase_key(A, heapsize, key)

a = [15,13,9,5,12,8,7,4,0,6,2,1]
print(a)
max_heap_insert(a,10)
print(a)


