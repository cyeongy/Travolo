# from collections import Counter
#
# t = []
# tt = Counter(t)
#
# print(len(tt))
# print(tt.most_common()[0][0])


import math

viet = []

while True:
    m = int(input())
    if m == 0:
        break
    viet.append(m)

print(viet)
answer = []


def check_prime(number):
    if number == 1:
        return False
    if number == 2:
        return True
    for i in range(2, int(math.sqrt(number)) + 1, 1):
        # print(i)
        if number % i == 0:
            return False
    return True


for m in viet:
    prime = 0
    for i in range(m + 1, 2 * m + 1):
        if check_prime(i):
            prime = prime + 1
    answer.append(prime)

for i in answer:
    print(i)
