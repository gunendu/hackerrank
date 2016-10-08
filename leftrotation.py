def main():
    n,d = map(int,raw_input().split())
    arr = map(int,raw_input().split())

    j = 0
    i = 0
    while(i<d):
        j = 0
        temp = arr[j]
        while(j<n-1):
            arr[j] = arr[j+1]
            j = j + 1
        arr[j] = temp
        i = i + 1

    arr = " ".join([str(x) for x in arr])

    print arr

main()
