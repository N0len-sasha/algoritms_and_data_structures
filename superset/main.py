def list_superset(list_set_1, list_set_2):
    if len(list_set_2) < len(list_set_1):
        list_set_1, list_set_2 = list_set_2, list_set_1
    for el in list_set_1:
        check = el in list_set_2
        if not check:
            break
    if check and len(list_set_2) == len(list_set_1):
        message = 'Наборы равны.'
    elif check:
        message = f'Набор {list_set_2} - супермножество.'
    else:
        message = 'Супермножество не обнаружено.'
    return message


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
