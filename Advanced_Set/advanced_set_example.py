s=set()
s.add(1)
s.add(2)
print(s)

s.clear()
print(s)

s1={1,2,3}
s2=s1.copy()
print(s2)

s3=set()
s3.add(1)
s3.add(2)
s3.add(3)
s3.add(4)
s3.add(5)

s4=s3.copy()
s3.add(6)
s3.add(7)

print(s3)
print(s4)

print(s3.difference(s4))

s5={1,2,3}
s6={1,6,7}
s5.difference_update(s6)
print(s5)

s6={1,2,3,4,5}
s6.discard(2)
print(s6)


s7={1,2,3,4,5}
s8={1,2,3}

print(s7.intersection(s8))

s7.intersection_update(s8)
print(s7)


s8={1,2,3,4}
s9={1,2}
s10={5}

print(s8.isdisjoint(s9))
print(s8.isdisjoint(s10))


s9={1,2,3}
s10={1}
print(s10.issubset(s9))
print(s9.issuperset(s10))


s11={1,2,3}
s12={1,2,3,4}
print(s11.symmetric_difference(s12))

s13={1,2}
s14={3,4}

print(s13.union(s14))
