s = 'Iterator'

itrobj = iter(s)

while True:
    try:
        print(next(itrobj))

    except StopIteration:
        break


