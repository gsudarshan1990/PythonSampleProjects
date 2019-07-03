from collections import Counter
list1=[1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4]
print(Counter(list1))

string1='aaaabbbbbcccccdddeeefff'
print(Counter(string1))

string3='Count the words in sentence number of words in present sentence'
words=string3.split()
print(Counter(words))

c=Counter(words)
print(c.most_common(4))
