# coding:utf-8
# cut rod (CLRS 15.1)

# cut rod  original recursion solution!
def cut_rod(p, n):
    if n == 0:
        return 0
    q = -1
    for i in range(1,n+1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q

# p = [0,1,5,8,9,10, 17,17,20,24,30]
# print(cut_rod(p,4))


# use dynamic programming for optimal rod cutting!
def memoized_cut_rod(p, n):
    r = [-1 for i in p]
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]

    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n+1):
            q = max(q, p[i]+ memoized_cut_rod_aux(p, n-i, r))
    r[n] = q
    return q

p = [0,1,5,8,9,10, 17,17,20,24,30]
for i in range(1,11):
    print(memoized_cut_rod(p,i))
