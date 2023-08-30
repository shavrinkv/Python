list_a = [1, 2, 3]
list_b = [11, 22, 33]

def list_gen(list_a, list_b):
 combined_list = [list_a, list_b]
 new_list = [i for sublist in combined_list for i in sublist]
 return new_list

print(list_gen(list_a, list_b))


values = [['a','a'], ['a','b','b'], ['a','b','b','a'], ['a','b','c','a','c']]
longest = 0
for value in values:
    longest = max(longest, len(value))

print(longest)