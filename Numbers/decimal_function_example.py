from decimal import Decimal

a=Decimal('4.2')
b=Decimal('2.1')
print(a)
print(b)
print(a+b)


from decimal import localcontext

a=Decimal('1.2')
b=Decimal('1.3')
print(b/a)

with localcontext() as ctx:
    ctx.prec=3
    print(b/a)


x = 1234.56789

print('{:0.2f}'.format(x))


print('{:10.3f}'.format(x))

x=1235

print(bin(x))
print(oct(x))
print(hex(x))
