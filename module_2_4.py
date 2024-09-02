numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime_ = []
not_primes = []
is_prime = True
n_ = 0
for i in numbers_:
    is_prime = True
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_.append(i)
        else:
            not_primes.append(i)
print('Primes:',prime_)
print('Not primes:',not_primes)