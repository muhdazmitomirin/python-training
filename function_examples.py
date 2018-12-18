#  FUNCTION DEFINITION

# def function_name(a, b, c):
#     <body of function>
#     return <return_value>


def add(a, b):
    total = a + b
    return total


def total(*args, **kwargs):
    ...


name = 'Jerry'
age = 20
total(nama=name, umur=age)
total(1, 2, 3, 4, 5)
total('hello', 'world')

add_a = add(1, 2)
add_b = add('hello ', 'world')
add_c = add(1.0, 3)

print(add_a, add_b, add_c)

