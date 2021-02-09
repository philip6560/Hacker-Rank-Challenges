toys_available_for_purchase = int(input('Enter the number of toys available for purchase:'))
marks_cash = int(input('How much do you have / What"s your budget :'))
price_list = []

for x in range(toys_available_for_purchase):
    each_price = int(input('Enter prices for each:'))
    price_list.append(each_price)


def mark_and_toys(prices, marks_money):
    possible_purchasable_toys = []
    purchasable = []
    toy_price_purchasable = 0
    accumulated_price = 0

    # loop to check for prices of Toys lesser than Mark's money
    for price in prices:
        if price <= marks_money:
            possible_purchasable_toys.append(price)
        else:
            continue

    # loop to sort the prices of Toys that Mark can purchase
    for i in range(len(possible_purchasable_toys)-1):
        for j in range(len(possible_purchasable_toys)-1):
            if possible_purchasable_toys[j] > possible_purchasable_toys[j+1]:
                possible_purchasable_toys[j], possible_purchasable_toys[j+1] = possible_purchasable_toys[j+1], possible_purchasable_toys[j]
            else:
                continue

    # loop to check the maximum number of Toys that Mark can purchase and the total price of these Toys
    for purchases in possible_purchasable_toys:
        accumulated_price = accumulated_price + purchases
        if accumulated_price <= marks_money:
            toy_price_purchasable = toy_price_purchasable + purchases
            purchasable.append(purchases)
        else:
            continue

    return (print('prices of toys purchasable with', marks_money, '=', possible_purchasable_toys),
            print('prices of toys purchased =', purchasable),
            print(len(purchasable), 'toys are purchasable at', toy_price_purchasable, 'unit of currency'),
            )


mark_and_toys(price_list, marks_cash)


