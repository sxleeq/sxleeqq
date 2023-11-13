n = int(input())
sum1 = 0
sum2 = 0
x = 1
for i in range(1, n + 1):
    sum1 += i ** 3
    for j in range(1, i + 1):
        x *= j
    sum2 += x
    x = 1
print(sum1)
print(sum2)