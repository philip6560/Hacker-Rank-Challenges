movements_list = []
count = int(input('How many times did ahvid move:'))
for moves in range(count - 1):
    values = input('Enter moves:').capitalize()
    movements_list.append(values)


def counting_valley(data_list, n):
    keyword = {
        'U': 1,
        'D': -1,
    }
    initial_location = 0
    current_location = [initial_location]
    initial_coordinates = []
    coordinates = []
    times_uphill = 0
    times_downhill = 0

    # loop used to determine ahvid's movement uphill and downhill
    for a in range(n - 1):
        if data_list[a] == 'U':
            initial_location = initial_location + keyword['U']
            current_location.append(initial_location)
            initial_coordinates = current_location[a], current_location[a + 1]

        elif data_list[a] == 'D':
            initial_location = initial_location + keyword['D']
            current_location.append(initial_location)
            initial_coordinates = current_location[a], current_location[a + 1]
        coordinates.append(initial_coordinates)

    # loop used to determine times ahvid's went up the hill and down the hill
    for b in range(len(current_location) - 1):
        if current_location[b] == 0 and current_location[b + 1] == keyword['U']:
            times_uphill = times_uphill + 1

        elif current_location[b] == 0 and current_location[b + 1] == keyword['D']:
            times_downhill = times_downhill + 1

    return (print('ahvid went up the hill', times_uphill, 'times'),
            print('ahvid went down the hill', times_downhill, 'times'),
            print('showing ahvids coordinates at each point: ', coordinates),
            print('movement uphill and downhill: ', current_location),
            )


counting_valley(movements_list, count)
