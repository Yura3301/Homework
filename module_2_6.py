import random
n = range(3,20)
random_n = random.choice(n)
result = []
for i in range(1,20):
    for j in range(1,20):
        if random_n % (i+j) == 0 and i < j:
            result.append(str(i))
            result.append(str(j))
            break
print('[',random_n,']', '[',''.join(result),']')