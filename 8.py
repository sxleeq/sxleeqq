n = int(input())
a = 0
x = 0
while x <= n:
    a += 1
    x = 1 << a
print(a - 1)