str_1 = 'test'
str_2 = 'test1'

print(f'"{str_2}" contains "{str_1}" = {str_1 in str_2}')
if str_2 in str_1:
    print(f'"{str_1}" нет "{str_2}"')
else:
    print(f'"{str_2}" да "{str_1}"')