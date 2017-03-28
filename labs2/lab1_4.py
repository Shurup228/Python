print("Insert first list: ")
lst1 = [int(x) for x in input().split()]
print("\nInsert second list: ")
lst2 = [int(x) for x in input().split()]


lst3 = lst1 + lst2
lst3.sort()
lst3 = lst3[::-1]

print(lst3)
