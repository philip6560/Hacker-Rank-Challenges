number_of_trips = int(input('Enter how many trips they are embarking on:'))
cash = 0
flavours_count = 0
data = 0


def what_flavours(cost_list, money):
    purchased = []
    r = 0

    for i in range(len(cost_list) - 1):
        r = r + 1
        for j in range(r, len(cost_list)):
            if cost_list[i] + cost_list[j] == money:
                purchased.append(i + 1)
                purchased.append(j + 1)
                print(cost_list)
                print('flavours purchased are at index', i + 1, ' ', j + 1)
            else:
                continue


for trip in range(number_of_trips):
    flavours_costs = []
    print()
    print('Trip ' + str(trip + 1) + ':')
    cash = int(input('How much did you guys come with:'))
    flavours_count = int(input('Enter how many flavours are available:'))
    for counts in range(flavours_count):
        data = int(input('Enter price for flavour ' + str(counts + 1) + ':'))
        flavours_costs.append(data)
    what_flavours(flavours_costs, cash)
