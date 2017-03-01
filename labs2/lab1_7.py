
def lab_function(input_string):
    input_string = str(abs(int(input_string)))
    lst_local = list(input_string)
    lst_local.sort()

    result_list = []

    while len(lst_local):
        const_first_val = lst_local[0]
        result_list.append((int(const_first_val), lst_local.count(const_first_val)))
        for elem in lst_local[:]:
            if elem == const_first_val:
                lst_local.remove(elem)
    return result_list

print(lab_function(input("Input your variable\n>> ")))






