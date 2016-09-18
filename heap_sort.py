# coding:utf-8

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i // 2) - 1

def heapsize(A):
    return len(A)

def max_heapify(A,heapsize,i):
    l = left(i)
    r = right(i)
    if l <= heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= heapsize and A[r] > A[largest]:
        largest = r
    
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        max_heapify(A,heapsize,largest)

def build_max_heap(A):
    heapsize = len(A) - 1 
    for i in range(parent(heapsize),-1,-1):
        max_heapify(A,heapsize,i)

def heap_sort(A):
    build_max_heap(A)
    heapsize = len(A) - 1 
    for i in range(len(A)-1,0,-1):
        A[i],A[0] = A[0],A[i]
        heapsize -= 1
        print(A)
        max_heapify(A,heapsize,0)

a = [5,13,2,25,7,17,20,8,4]
print(a)
heap_sort(a)
print(a)
        
        
        
        







        
    
    

