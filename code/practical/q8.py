'''
8. WAP to find the prime factors of a number.
'''
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors
n=int(input("Enter a number:-"))
print("Prime factors:-",prime_factors(n))