fact1 = lambda n: 1 if n <= 1 else n * fact1(n - 1)
print(fact1(3))


def fact2(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return n * fact2(n - 1)


print(fact2(3))
