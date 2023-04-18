from random import choice
from string import ascii_lowercase

chars = ascii_lowercase + ascii_lowercase
lst = [''.join(choice(chars) for _ in range(5)) for _ in range(100)]
lst.sort()
print(lst)

