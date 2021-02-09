data_length = int(input('Enter the length of the list to be sorted:'))
data_list = []

for x in range(data_length):
    x = int(input('Enter number:'))
    data_list.append(x)


def bubble_sort(data_set, array_count):
    swap_count = 0
    for i in range(array_count):
        for j in range(array_count - 1):
            if data_set[j] > data_set[j+1]:
                data_set[j], data_set[j+1] = data_set[j+1], data_set[j]
                swap_count = swap_count + 1
            else:
                continue

    return (print('Array is sorted in', swap_count, 'swaps'),
            print('First Element:', data_set[array_count-array_count]),
            print('Last Element:', data_set[array_count-1])
            )


bubble_sort(data_list, data_length)
