

def qsort(a):
    if not a:
        return []

    middle = [x for x in a if x == a[0]]
    lesser = qsort([x for x in a if x < a[0]])
    greater = qsort([x for x in a if x > a[0]])

    return lesser + middle + greater

a = [1, 4, 3, 3,6]
print(qsort(a))