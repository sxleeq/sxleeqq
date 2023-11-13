n, k = map(int, input().split())
a = 0
b = 0
kol = k
sum1 = 0
sum2 = 0
maxi = -100 * 100
mini = 100 * 100
while a != n:
    c = int(input())
    if b < k:
        sum1 += c
        sum2 += 1 / c
        if c > maxi:
            maxi = c
        if c < mini:
            mini = c
    a += 1
    b += 1
print(sum1 / kol) # среднее арифметическое
print(2 / sum2) # среднее гармоническое
print(maxi) # максимальный элемент
print(mini) # минимальный элемент