from calendar import c
from collections import Counter
from itertools import count
l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

p = "palabares"
print(Counter(p))

animales = "gato perro canario perro canario perro"
print(Counter(animales))

c = Counter(animales.split())

c.most_common(2)
print(c)

l = [10,20, 30, 40, 10, 20, 30, 10, 20, 10]
c = Counter(l)
c.items()
c.keys()
print(c) 

