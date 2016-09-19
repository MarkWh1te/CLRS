# coding:utf-8


from quick_sort import partition

def randomized_partition(A,p,r):
    from random import randint
    i = randint(p,r)
    A[r],A[i] = A[i],A[r]
    return partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p < r:
        print(p,r)
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q-1)
        randomized_partition(A,q+1,r)


a = [2,1,10,9,8,7] 
print(a)
randomized_quicksort(a,0,len(a)-1)
print(a)

    
    
    
    

