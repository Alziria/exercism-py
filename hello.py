my_first_variable = 1
print(my_first_variable)
my_first_variable = 2
print(my_first_variable)
print("Hello World!")
# Hello World!
my_second_variable = 3
print(my_second_variable)
# 3
my_second_variable = "Now I'm a string."
print(my_second_variable)
# Now I'm a string.
import collections
import random
my_second_variable = collections.Counter([random.randint(0,100) for _ in range(1000)])
print(my_second_variable)
