"""
For example, suppose you have a list of words and you want to sort them from
longest to shortest:

'but soft what light in yonder window breaks'

"""

line='but soft what light in yonder window breaks'
words=line.split()
words_len_list=list()
for word in words:
    words_len_list.append((len(word),word))
print(words_len_list)
sorted_list=sorted(words_len_list,reverse=True)
print(sorted_list)

for length,word in sorted_list:
    print(word)
