s='hello'

s_iter=iter(s)

for i in range(len(s)):
    print(next(s_iter))


word="Be a Good Human Being"
word_iter=iter(word)

for i in range(len(word)):
    print(next(word_iter))
