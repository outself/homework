def sort_array(arr):
    for i in range(len(arr) - 1):
        #print(range(len(arr) - i - 1))
        for j in range(len(arr) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            #print([i, j])
    return a


def max_value(a, b):
    return a if a > b else b


print(max_value(2, 6))

#a = [82, -5, 35, 9]
#print(sort_array(a))