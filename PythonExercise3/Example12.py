"""
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
"""

def check_number_prime(number):

    flag=False
    for i in range(2,int(number/2)+1):
        if (number%i == 0):
            flag=True
            break
    if not flag:
        print(str(number)+"is prime")
        return number


def count_primes(allnumbers):
    prime_number_list=[]
    for i in range(2,allnumbers+1):
        prime_number=check_number_prime(i)
        if prime_number != None:
            prime_number_list.append(prime_number)
    print(len(prime_number_list))


count_primes(100)




