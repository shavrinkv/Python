from random import randint

random_list = [randint(1, 50) for i in range(5)]
print(random_list)


random_list.append('десять')
print(random_list)


random_list.reverse()
print(random_list)



