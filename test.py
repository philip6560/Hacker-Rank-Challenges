counter = int(input())
data_list = list(map(int, input().split()))


def jumping_on_clouds(moves_list, n):
    keywords = {
        'safe': 0,
        'danger': 1,
    }
    path_a = []
    path_b = []
    count = 0
    # steps to determining path_a i.e the n+1 and n+2 path
    for moves in range(n - 2):
        if moves_list[moves] == keywords['safe'] and moves == count:
            if moves_list[moves + 1] == keywords['safe'] and moves_list[moves + 2] == keywords['danger']:
                moves_1 = moves + 1
                count = moves + 1
                path_a.append(moves_1)

            elif moves_list[moves + 1] == keywords['danger'] and moves_list[moves + 2] == keywords['safe']:
                moves_2 = moves + 2
                count = moves + 2
                path_a.append(moves_2)

            elif moves_list[moves + 1] == keywords['safe'] and moves_list[moves + 2] == keywords['safe']:
                moves_3 = moves + 2
                count = moves + 2
                path_a.append(moves_3)

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
            path_b.append(len(moves_list))

            # check to determine which path has minimum moves
            if len(path_a) > len(path_b):
                minimum_moves = len(path_b)
                return minimum_moves

            elif len(path_a) < len(path_b):
                minimum_moves = len(path_a)
                return minimum_moves

            else:
                minimum_moves = len(path_a) or len(path_b)
                return minimum_moves
        else:
            minimum_moves = len(path_a)
            return minimum_moves


result = jumping_on_clouds(data_list, counter)
print(result)

