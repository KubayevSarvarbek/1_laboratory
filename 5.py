from random import choice
from string import ascii_lowercase
import random

text_f = ascii_lowercase + ascii_lowercase
text = [''.join(choice(text_f) for i in range(3)) for i in range(3)]

randomlist = random.sample(range(10, 99), 3)

float_number = round(random.uniform(11.11, 99.99), 2) 

print(text)
print(type(text[0]))
print('//////')
print(randomlist)
print(type(randomlist[0]))
print('//////')
print(float_number)
print(type(float_number))