rows = int(input('Enter number of array rows:'))
cols = int(input('Enter number of array columns:'))
data_set = []

for n in range(rows):
    data_set.append([])
for b in range(rows):
    for c in range(cols):
        data = int(input('Enter value for row ' + str(b + 1) + ':'))
        data_set[b].append(data)


def max_number_2d_array(data_list):
    top = []
    middle = []
    bottom = []
    hour_glass_total = []
    counter = int(len(data_list) - 3)
    middle_counter = 0
    bottom_counter = 1
    # structure of the hour_glass is a b c
    #                                  d
    #                                e f g
    # top_counter accounts for the topmost structure of the hour_glass i.e  a b c
    # middle_counter accounts for the middle structure of the hour_glass i.e  d
    # bottom_counter accounts for the bottom structure of the hour_glass i.e e f g
    # loop counting the individual lists in the datalist
    for top_counter in range(len(data_list) - 1):
        middle_counter = middle_counter + 1
        bottom_counter = bottom_counter + 1
        inner_counter = 0
        inner_top_counter = 0
        inner_middle_counter = 1
        inner_bottom_counter = 2
        # conditional statement to check and make sure the underlying statements are executed 4 times
        # where top_counter = 0 to 3 and counter = 3

        if top_counter < counter:
            # loop counting the individual elements in each individual list in the datalist
            for element_counter in range(len(data_list[top_counter]) - 1):
                # conditional statement to check and make sure the underlying statements are executed 4 time
                # where inner_counter = 0 to n and element_counter = 0 to n+1
                if inner_counter < element_counter:
                    # top[] stores all topmost values of the hour_glass structure
                    top.append(data_list[top_counter][inner_top_counter:inner_bottom_counter + 1])
                    # middle[] stores all the middle values of the hour_glass structure
                    middle.append(data_list[middle_counter][inner_middle_counter])
                    # bottom[] stores all the bottommost values of the hour_glass structure
                    bottom.append(data_list[bottom_counter][inner_top_counter:inner_bottom_counter + 1])
                    inner_counter = inner_counter + 1
                    inner_top_counter = inner_top_counter + 1
                    inner_middle_counter = inner_middle_counter + 1
                    inner_bottom_counter = inner_bottom_counter + 1
                else:
                    continue
        else:
            continue
        # summing the top, middle and bottom values for the hour glass structure i.e 'a b c'
        #                                                                              d
        #                                                                             e f g
    for x in range(len(top)):
        a = sum(top[x]) + middle[x] + sum(bottom[x])
        hour_glass_total.append(a)

        # sort the list of hour_glass_total values in descending order to get the max_hour_glass value
    for i in range(len(hour_glass_total) - 1):
        for j in range(len(hour_glass_total) - 1):
            if hour_glass_total[j] < hour_glass_total[j + 1]:
                # swapping values at j+1 to j i.e lower values for higher values
                hour_glass_total[j], hour_glass_total[j + 1] = hour_glass_total[j + 1], hour_glass_total[j]
            else:
                continue
    max_hour_glass_value = hour_glass_total[0]

    return (print(hour_glass_total),
            print(max_hour_glass_value))


max_number_2d_array(data_set)


