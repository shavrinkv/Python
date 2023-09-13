def intersection(lst1, lst2):
        lst3 = list(filter(lambda x: x in lst1,lst2))
        return lst3
lst1 = [1, 4, 6, 7, 12, 27, 41]
lst2 = [13, 17, 27, 34, 41, 56]
print(intersection(lst1, lst2))