def n1():
    name = str(input())
    age = int(input())
    if age < 7:
        print('entrepreneur')
    elif 7 <= age <= 14:
        print('Hello, ', name, '! You are in', (age % 7) + 1, 'klass')
    elif 7 <= age <= 17:
        print('Hello, ', name, '! You are in', (age % 7) + 1, 'klass and you have', (age % 15) + 1,
              'years of programing experience. Sounds cool!')
    elif 18 <= age <= 21:
        print('Hello, ', name, '! You are at', (age % 18) + 1, 'course and you have', (age % 15) + 1,
              'years of programing experience. Sounds cool!')
    else:
        print('Hello, ', name, '! You are entrepreneur and you have', (age % 15) + 1,
              ' years of programing experience. Sounds cool!')


def n2():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return abs(a * b) // gcd(a, b)
    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))


def n3():
    n, k = map(int, input().split())
    a = 0
    b = 0
    d = []
    kol = k
    sum1 = 0
    sum2 = 0
    while a != n:
        c = int(input())
        if b < k:
            sum1 += c
            sum2 += 1 / c
            d.append(c)
        a += 1
        b += 1
    e = sorted(d)
    maxi = e[-1]
    maxi1 = e[-2]
    mini = e[0]
    mini1 = e[1]
    print(sum1 / kol)  # среднее арифметическое
    print(2 / sum2)  # среднее гармоническое
    print(maxi)  # максимальный элемент
    print(maxi1)  # 2 максимальный элемент
    print(mini)  # минимальный элемент
    print(mini1)  # 2 минимальный элемент


def n4():
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
    if n == 0:
        sum2 = 1
    print(sum1)
    print(sum2)


def n5():
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


def n6():
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)

    n = int(input())
    print(fib(n))


def n8():
    n = int(input())
    a = 0
    x = 0
    while x <= n:
        a += 1
        x = 1 << a
    print(a - 1)


def n9():
    h, a, b = map(int, input().split(";"))
    print((h - a) // (a - b) + 1)


def n10():
    gr = float(input()) * 2
    h = int(gr // 60)
    m = int(gr % 60)
    s = int(((gr % 30) % 0.5) * 120)
    print(h, 'h', m, 'm', s, 's')


n = int(input('Введите номер задачи'))
if n == 1:
    n1()
if n == 2:
    n2()
if n == 3:
    n3()
if n == 4:
    n4()
if n == 5:
    n5()
if n == 6:
    n6()
if n == 7:
    print("doesn't work")
if n == 8:
    n8()
if n == 9:
    n9()
if n == 10:
    n10()
