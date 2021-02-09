string_count = int(input('Enter the number of times to repeat string characters:'))
data_list = input('Enter strings e.g aba or abb :')


def repeated_string(string_list, repeating_times):
    repeated_list = []
    # loop showing how the strings are repeated and added to the list
    for rep in range(len(string_list)):
        for x in string_list:
            if len(repeated_list) < repeating_times:
                repeated_list.append(x)
            else:
                break
    return print(repeated_list)


repeated_string(data_list, string_count)
