from fluff import bubble_sorter, quicksorter, insertion_sorter


list1 = [9,1,2,3]
list2 = [1,4,5,6]


def sumlists(lst1, lst2):
    count = 0
    if len(lst1) > len(lst2):
        lst = list(lst1)
    else:
        lst = list(lst2)
    while count < len(lst1) and count < len(lst2):
        lst[count] = lst1[count] + lst2[count]
        print("out list", lst)
        count += 1
        print("count =", count)
    return lst

readylist = sumlists(list1, list2)

print("quicksorter", quicksorter.qsort(readylist))
print("bubblesorter", bubble_sorter.bubblesorter(readylist).sort())
print("insertionsorter", insertion_sorter.ins_sort(readylist))