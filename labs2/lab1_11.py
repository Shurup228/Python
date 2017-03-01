
lst1 = [int(x) for x in input().split()]
lst2 = [int(x) for x in input().split()]

lst1.sort(), lst2.sort()

set1 = set(lst1)
set2 = set(lst2)

lst_result = list(set1.intersection(set2))

if len(lst1) != 0 and len(lst2) != 0:
    print(lst_result)
else:
    print("lists are empty")