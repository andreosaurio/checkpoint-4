from decimal import Decimal
import math

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ['name', 'surname', 'user', 'password']

my_tuple = ('name', 'surname', 'user', 'password')

my_float = 8.7

my_integer = 8

my_decimal = Decimal(8.8787655)

my_dictionary = {
  'user1': 'Andrea',
  'user2': 'Mikel',
  'user3': 'Jon'
}

# Exercise 2: Round your float up.

my_rounded_float = math.ceil(my_float)

# Exercise 3: Get the square root of your float.

my_float_sqrt = math.sqrt(my_float)

# Exercise 4: Select the first element from your dictionary.

my_dictionary_first = my_dictionary['user1']

# Exercise 5: Select the second element from your tuple.

my_tuple_second = my_tuple[1]

# Exercise 6: Add an element to the end of your list.

my_list.append('age')

# Exercise 7: Replace the first element in your list.

my_list[0] = 'address'

# Exercise 8: Sort your list alphabetically.

my_list.sort()

# Exercise 9: Use reassignment to add an element to your tuple.

my_new_tuple = my_tuple + ('age',)