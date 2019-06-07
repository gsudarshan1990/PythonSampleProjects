print('Let\'s practice everything')
print('You\'d need to know \' about escapes with \\ that do \n newlines and \t tabs \'')
poem="\t The lovely world\n" \
     "with logic so firmly planted" \
     "cannot discern \n the needs of lover" \
     "nor comprehend passion with intuition \nand requires an" \
     "explanation \n\t\t where there is none"

print('-'*10)
print(poem)
print('-'*10)

five=10-2+3-6
print(five)

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates

starting_point=10000
beans,jars,crates=secret_formula(starting_point)
print(f'{beans} beans, {jars} jars,{crates} crates')

starting_point=10000/10
beans,jars,crates=secret_formula(starting_point)
print(f'{beans} beans, {jars} jars,{crates} crates')
