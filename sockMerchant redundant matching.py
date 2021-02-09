no_of_socks = int(input('Enter how many sock your are sorting based on colours:'))
socks_for_sorting = list(map(int, input('Enter colour codes:').split()))


def sock_merchant(num, sorted_sock):
    pair = []
    i = 1
    j = 1
    for a in range(num - 1):
        for n in range(num - 1):
            if sorted_sock[n] > sorted_sock[n + i]:
                swap = sorted_sock[n + i]
                sorted_sock[n + i] = sorted_sock[n]
                sorted_sock[n] = swap
            else:
                continue
    for b in range(len(sorted_sock) - 1):
        for m in range(len(sorted_sock) - 1):
            if sorted_sock[m] == sorted_sock[m + j]:
                pair.insert(0, sorted_sock[m])
                pair.insert(0, sorted_sock[m + j])
                del (sorted_sock[m + j], sorted_sock[m])
                break
            else:
                continue
    print(pair)
    total_pair = int(len(pair) / 2)
    return total_pair


result = sock_merchant(no_of_socks, socks_for_sorting)
print(result)



