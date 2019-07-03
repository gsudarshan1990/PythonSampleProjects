
def money_format(argument_func):
    def wrapper(*args,**kwargs):
        r=argument_func(*args,**kwargs)
        formatted='${:.2f}'.format(r)
        return formatted
    return wrapper

@money_format
def add_tax(value,tax):
    return value*(1+(tax/100))

print(add_tax(52,20))
print(add_tax(10,10))
