def get_list_of_multiples(numbers, m):

    if len(numbers) > 1:
        if(numbers[0] % m == 0):
            return [numbers[0]] + get_list_of_multiples(numbers[1:], m)
        return get_list_of_multiples(numbers[1:], m)
    elif(numbers[0] % m == 0):
        return [numbers[0]]
    else:
        return []


print(get_list_of_multiples([2, 3, 5, 6], 2))