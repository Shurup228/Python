

def ins_sort(k):
    for i in range(1, len(k)):
        j = i
        while j > 0 and k[j] < k[j-1]:
            k[j], k[j-1] = k[j-1], k[j]
            j -= 1
    return k

print(ins_sort([2,2,1,5]))
