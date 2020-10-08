# Проверка скорости выполнения

import timeit

code_to_test = '''
def fact(n):
    res = 1
    for el in range(1, n + 1):
        res *= el
        yield res
        
        
a = [el for el in fact(60)]
'''
elapsed_time = timeit.timeit(code_to_test, number=1000) / 1000
print(elapsed_time)

code_to_test = '''
def fact2(n):
    res = 1
    count = 1
    while count <= n:
        res *= count
        count += 1
        yield res

a = [el for el in fact2(60)]
'''
elapsed_time = timeit.timeit(code_to_test, number=1000) / 1000
print(elapsed_time)

code_to_test = '''
import random
in_list = [random.randint(0, 1000) for i in range(1, 1000)]
res = [el for el in in_list if in_list.count(el) == 1]
'''
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)


code_to_test = """
import random
in_list = [random.randint(0, 1000) for i in range(1, 1000)]
no_double_indexes = [el for el in range(0, len(in_list))]  # список индексов
i = 0
len_change = False
while i < len(no_double_indexes):
    i_in = i + 1
    len_change = False
    len_no_double_indexes = len(no_double_indexes)
    while i_in < len_no_double_indexes:
        if in_list[no_double_indexes[i]] == in_list[no_double_indexes[i_in]]:
            no_double_indexes.remove(no_double_indexes[i_in])
            len_no_double_indexes = len(no_double_indexes)
            len_change = True
        else:
            i_in += 1
    if len_change:
        no_double_indexes.remove(no_double_indexes[i])
    else:
        i += 1
res = [in_list[i] for i in no_double_indexes]
"""

elapsed_time = timeit.timeit(code_to_test, number=100)/100
print(elapsed_time)

code_to_test = '''
import random
in_list = [random.randint(0, 1000) for i in range(1, 1000)]
i = 0
is_double = False
res = []
len_list = len(in_list)
while i < len_list:
    i_in = 0
    is_double = False
    while i_in < len_list:
        if in_list[i] == in_list[i_in] and i != i_in:
            is_double = True
        i_in += 1
    if not is_double:
        res.append(in_list[i])
    i += 1

'''
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)

code_to_test = '''
import random
in_list = [random.randint(0, 1000) for i in range(1, 1000)]
i = 0
res = []
len_list = len(in_list)
for i, el in enumerate(in_list):
    is_double = False
    for i_in, el_in in enumerate(in_list):
        if el_in == el and i != i_in:
            is_double = True
    if not is_double:
        res.append(el)

'''
elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)
