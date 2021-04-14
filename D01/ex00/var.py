def var():
    nbr_1 = 42 
    str_1= '42'
    str_2 = 'quarante-deux'
    nbr_2 = 42.0
    bool_1 = True
    list_1 = [42]
    dict_1 = {42: 42}
    tuple_1 = (42,)
    set_1 = set()
    print(nbr_1, 'est de type ', type(nbr_1))
    print(str_1, 'est de type ', type(str_2))
    print(str_2, 'est de type ', type(str_2))
    print(nbr_2, 'est de type ', type(nbr_2))
    print(bool_1, 'est de type ', type(bool_1))
    print(list_1, 'est de type ', type(list_1))
    print(dict_1, 'est de type ', type(dict_1))
    print(tuple_1, 'est de type ', type(tuple_1))
    print(set_1, 'est de type ', type(set_1))

if __name__ == '__main__':
    var()