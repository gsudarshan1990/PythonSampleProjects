s='hello'

s_iter=iter(s)

for i in range(len(s)):
    print(next(s_iter))
