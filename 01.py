from collections import Counter

# Данная функция должна подходить под описание обеих функций из задания
def buyers_count(n_customers, n_first_id=0):
    group_numbers = []

    for i in range(n_customers):
        group_number = 0
        current_id = n_first_id + i
        for j in range(len(str(current_id))):
            group_number += current_id % 10
            current_id = current_id // 10
        group_numbers.append(group_number)

    groups_count = Counter(group_numbers)
    for i in dict(groups_count):
        print("{} : {}".format(i, dict(groups_count)[i]))


