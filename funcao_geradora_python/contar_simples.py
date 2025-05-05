def contar_ate_tres():
    a = yield 1
    b = yield 2
    c = yield 3

contar = contar_ate_tres()
print(next(contar))
print(next(contar))
print(next(contar))
