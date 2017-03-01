
a = [int(x) for x in input().split()] # вводим с клавиатуры список



def swapp(lst):
    max = lst[0]
    min = lst[0]
    minindex = 0
    maxindex = 0
    for elem in lst:
        if elem > max:
            max = elem
            maxindex = lst.index(elem)
        if elem < min:
            min = elem
            minindex = lst.index(elem)
    lst[minindex], lst[maxindex] = lst[maxindex], lst[minindex]

    return lst

mylist = swapp(a)
mytuple = tuple(mylist)
print(mytuple)