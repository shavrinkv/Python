list1 = [1, 2, 3, -4, -5]
pos_count, neg_count = 0,0
for num in list1:
    if num >= 0:
        pos_count += 1
    else:
        neg_count += 1

print('Количество положительных чисел: ', pos_count)