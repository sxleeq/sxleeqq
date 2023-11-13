K = input()
N = int(input()) - 1

while N:
    num1 = [K[0]]
    k = 0
    for i in range(1, len(K)):
        if K[i] != K[i - 1]:
            num1.append(K[i])
            k += 1
        else:
            num1[k] += K[i]
    K = ''
    for z in num1:
        K += str(len(z)) + z[0]
    N -= 1

print(' '.join(K))