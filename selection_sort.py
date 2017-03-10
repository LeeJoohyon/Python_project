def selection_sort(array):
    for i in range(0, len(array) - 1):
        min_index = find_min_index(array, i)

        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

    return array


def find_min_index(array, i):
    min = array[i]
    min_index = i
    for j in range(i + 1, len(array)):
        if (array[j] < min):
            min = array[j]
            min_index = j

    return min_index


array = [5, 1, 3, 8, 2]
print
'before :', array
sorted_array = selection_sort(array)
print
'sorted array :', sorted_array