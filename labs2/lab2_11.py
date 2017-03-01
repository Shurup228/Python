lst = [(), ()]

dict_ = {}
if len(lst) and len(lst[0]):
    for each in lst:
        if each[1] in dict_:
            dict_[each[1]].append(each[0])

        else:
            dict_[each[1]] = [each[0]]


print(dict_)
for each in dict_:
    print(each, len(dict_[each]))

