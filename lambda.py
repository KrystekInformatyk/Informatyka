def pierwsze(lst1, lst2, les3):
    sr = lambda lst: sum(lst)/len(lst)
    all_lst = [lst1,lst2,les3]
    w = []
    for lst in all_lst:
        w.append(sr(lst))
    return w.index(max(w))

print(pierwsze([1,2,3,4,5],[-2,-3,-6],[20]))

from random import randint
drugie = lambda k,n,m: [randint(n,m) for i in range(k)]
print(drugie(10,10,20))

trzecie = lambda lst: list(map(lambda el: el**2, lst))
print(trzecie([2,3,4,5,6,7,8]))

czwarte = lambda lst: list(map(lambda el: el**1/2, lst))
print(czwarte([4,8,16]))
