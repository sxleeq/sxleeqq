n = int(input())
a = int(input())
if a != 1:
    ans = 1
else:
    ans = n
for i in range(n - 2):
    x = a
    a = int(input())
    if a - x != 1:
        ans = a - 1
print(ans)