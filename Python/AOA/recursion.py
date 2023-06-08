fact1 = lambda n: 1 if n <= 1 else n * fact1(n - 1)
print(fact1(3))


def fact2(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fact2(n - 1)


print(fact2(3))


def fibo(data: int) -> int:
    if data in [0, 1]:
        return data
    return fibo(data - 1) + fibo(data - 2)


def fibo_memo(data: int, memo: dict = {}) -> int:
    if data in [0, 1]:
        return data
    if data in memo:
        return memo[data]

    memo[data] = fibo(data - 1) + fibo(data - 2)
    return memo[data]


print(fibo(6))
print(fibo_memo(6))
