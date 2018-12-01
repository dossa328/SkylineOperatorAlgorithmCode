def call():
    print(fibonachi(10))


def fibonachi(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    re = fibonachi(n-1) + fibonachi(n-2)

    return re
