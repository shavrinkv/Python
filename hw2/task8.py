from operator import itemgetter
def Sort_Tuple(tup):
    return (sorted(tup, key=itemgetter(2)))
tup = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print(Sort_Tuple(tup))