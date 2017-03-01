a = [int(x) for x in input("Input your list\n> ").split()]
b = int(input("Input your key value to start\n> "))


def task_func(lst1, x):
    lst2 = []
    for elem in lst1:
        if elem <= x:
            lst2.append(elem)
    return lst2


def bubble_sort(lst):
    for first in range(len(lst)):
        for sec in range(len(lst) - 1):
            if (lst[first] < lst[sec]):
                lst[first], lst[sec] = lst[sec], lst[first]
    return lst


def insertion_sort(lst):
    for elem in range(1, len(lst)):

        currentvalue = lst[elem]
        position = elem

        while position > 0 and lst[position - 1] > currentvalue:
            lst[position] = lst[position - 1]
            print(lst)
            position -= 1

        lst[position] = currentvalue
    return lst


def selection_sort(lst):
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if (lst[i] > lst[j]):
                lst[i], lst[j] = lst[j], lst[i]
    return lst


target_list = task_func(a, b)

print("Bubblesort:", bubble_sort(target_list), "\n",
      "Insertionsort:", insertion_sort(target_list), "\n",
      "Selectionsort:", selection_sort(target_list))
