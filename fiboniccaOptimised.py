def fibonnica(n):
    if n <= 1:
        return 1

    if f[n]:
        return f[n]

    f[n] = fibonicca(n-1) + fibonicca(n-2)

    print f[n]


while True:
    n = int(raw_input())
    fibonicca(n)
