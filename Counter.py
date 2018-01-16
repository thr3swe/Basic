from collections import Counter
c = Counter('hello world')
print (c)
#Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
print (c.most_common(2))
#[('l', 3), ('o', 2)]