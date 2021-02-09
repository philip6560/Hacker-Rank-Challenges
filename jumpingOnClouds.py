counter = int(input('Enter the number total number of moves:'))
data_list = []

for num in range(counter):
    count = int(input('Enter moves as 0 or 1:'))
    data_list.append(count)


def jumping_on_clouds(moves_list, n):
    keywords = {
        'safe': 0,
        'danger': 1,
    }
    starting_point = 0
    path_a = [starting_point]
    path_b = [starting_point]

    # steps to determining path_a i.e the n+1 and n+2 path
    for moves in range(n - 1):
        if moves_list[moves] == keywords['safe']:
            if moves_list[moves + 1] == keywords['safe']:
                moves_1 = moves + 1
                path_a.append(moves_1)

            elif moves_list[moves + 1] == keywords['safe'] or moves_list[moves + 2] == keywords['safe']:
                path_a.append(moves + 2)
            else:
                continue
        else:
            continue
    # steps to determining path_b i.e the n+2 path
    for moves in range(n - 2):
        if moves_list[moves] == keywords['safe']:
            if moves_list[moves + 2] == keywords['safe']:
                moves_2 = moves + 2
                path_b.append(moves_2)
            else:
                continue
        else:
            continue

    # check to make sure path_b is a complete path
    for vert in range(len(path_b) - 1):
        if path_b[vert + 1] % 2 == 0 and sum(path_b) % 2 == 0:
            path_b.append(len(moves_list) - 1)

            # check to determine which path has minimum moves
            if len(path_a) > len(path_b):
                minimum_moves = len(path_b)
                print('1st path = ', path_a, '   ', '2nd path', path_b)
                print(minimum_moves, 'is the minimum move required')
                break

            elif len(path_a) < len(path_b):
                minimum_moves = len(path_a)
                print('1st path = ', path_a, '   ', '2nd path', path_b)
                print(minimum_moves, 'is the minimum move required ')
                break

            else:
                minimum_moves = len(path_a) or len(path_b)
                print('1st path = ', path_a, '   ', '2nd path', path_b)
                print(minimum_moves, 'is the minimum move required')
                break
        else:
            minimum_moves = len(path_a)
            print('Path = ', path_a)
            print(minimum_moves, 'is is the minimum move required')
            break


jumping_on_clouds(data_list, counter)



