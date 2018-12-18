# LIST is mutable

list_a = ['a', 'b', 'c']
list_b = list('d', 'e', 'f')

#  print(len(list_a))
#  print(len(list_b))

list_c = [1, 2, 3, 4, 5]

# LIST COMPREHENSION
list_d = [i*i for i in list_c]

list_a.extend(list_b)
print(list_a)

# LIST OPERATION
empty_list = list()
empty_list.append('a')
empty_list.append('b')

#  print(empty_list)





