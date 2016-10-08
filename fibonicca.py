def fibonicca(n):
    list1 = []
    list1.append(0)
    list1.append(1)
    i = 2
    while(i<=n):
        list1.append(list1[i-2] + list1[i-1])
        i = i + 1
    return list1

def main():
    n = int(raw_input())
    v = fibonicca(n)
    print v[n]

main()
