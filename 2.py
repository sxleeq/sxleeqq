a, b = map(int, input().split())
while a != 0 and b != 0:
    if a > b:
        a=a%b
    else:
        b = b % a
while a != 0 and b != 0:
    if a > b:
    else:
        b = b % a
gcd = a + b
print(gcd)
