from random import randint
def TAN(N):
    i = 1
    while N:
        yield randint(10000,999999)
        i += 1
        N = N-1

itrobj = TAN(int(input()))
tan_list = []

while True:
    try:
        tan_list.append(next(itrobj))

    except StopIteration:
        break

print(tan_list)
