from itertools import permutations
from collections import defaultdict
dict = defaultdict
T = int(input())

MAX_N = 50
a = [0] * MAX_N
b = [0] * MAX_N
c = [0] * MAX_N
__a = [0] * MAX_N
__b = [0] * MAX_N
__c = [0] * MAX_N

min_abc = [0] * MAX_N


for _ in range(T):
    n = int(input())
    answer = int(10e11)
    tot = 1000000000
    idxs = dict(list)
    for i in range(n):
        _a, _b, _c = map(int, input().split())
        # _a, _b, _c = 1000000, 1000000, 1000000
        a[i] = _b + _c
        b[i] = _a + _c
        c[i] = _a + _b
        min_abc[i] = min(a[i], b[i], c[i])
    

    if n <= 2:
        print(-1)
        continue
    iter = permutations(range(3), 3)
    for i, j ,k in iter:
        temp = a[i] + b[j] + c[k]
        tot = min(tot, temp)
        if tot == temp:
            idxs['a'] = [i]
            idxs['b'] = [j]
            idxs['c'] = [k]
    print(idxs)
 