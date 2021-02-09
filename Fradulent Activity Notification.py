days_count = int(input('Enter the number of days you want to monitor client"s transaction:'))
transaction_data_set = []
data = 0
trailing_counter = int(input('Enter the days interval for trailing client"s expenditure:'))
for x in range(days_count):
    data = input('Enter amount for day ' + str(x+1) + ':')
    transaction_data_set.append(data)


def fraud_notifier(transaction_data, trailing_days, days_number):
    notification_box = 0
    start = trailing_days - trailing_days
    end = trailing_days
    prior_transact_data = []
    i = 0
    median = 0

    # main loop in the function checking for fraud based on the number of days given
    for trail in range(days_number):
        # check to start monitoring transaction history when trail >= trailing days
        if trail >= trailing_days:
            client_spends = int(transaction_data[trail])
            prior_transact_data.append(transaction_data[start:end])
            start = start + 1
            end = end + 1
            # sub-loop to sort transaction record for each trail(day client spends) in ascending order
            # i serves as the trail counter i.e counter for each day
            for i in range(len(prior_transact_data)):
                # sub-loop serves as enables swapping and sorting of the data
                for j in range(len(prior_transact_data[i]) - 1):
                    for k in range(len(prior_transact_data[i]) - 1):
                        if prior_transact_data[i][k] > prior_transact_data[i][k + 1]:
                            prior_transact_data[i][k], prior_transact_data[i][k + 1] = prior_transact_data[i][k + 1], \
                                                                                       prior_transact_data[i][k]
                        else:
                            continue
            # check to determine if the median is odd
            if trailing_days % 2 != 0:
                middle_num = int(trailing_days / 2)
                median = int(prior_transact_data[i][middle_num])
                print(median, client_spends)
                # check to determine if fraud notification would be sent to our client
                if client_spends >= 2 * median:
                    notification_box = notification_box + 1
                else:
                    continue
            # check to determine if the median is even
            elif trailing_days % 2 == 0:
                middle_num = int(trailing_days / 2)
                median_sum = int(prior_transact_data[i][middle_num - 1] + prior_transact_data[i][middle_num])
                median = median_sum / 2
                # check to determine if fraud notification would be sent to our client
                if client_spends >= 2 * median:
                    notification_box = notification_box + 1
                else:
                    continue
            else:
                continue
        else:
            continue
    return print('notification_box:', notification_box)


fraud_notifier(transaction_data_set, trailing_counter, days_count)



