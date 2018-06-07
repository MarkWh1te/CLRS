# encoding:utf-8


def counting_sort(A,k):
    print(len(A),A[10])
    C = [0 for i in  range(k+1)]
    B = [0 for i in range(len(A))]
    for i in range(0,len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]

    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B
    
a = [6,0,2,0,1,3,4,6,1,3,2]
print(a)
print(counting_sort(a,max(a)))

    
    
    
