from collections import Counter
#print ("Write a word")
c=raw_input("Write a word\n")
#c = Counter('hello world')
a = Counter(c)
print (a)
#Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
print ("Most common are ")
print (a.most_common(3))
#[('l', 3), ('o', 2)]