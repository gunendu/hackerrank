def decoupled(arr):
    xor = arr[0]
    for i in range(1,len(arr)):
        xor = xor ^ arr[i]

    print xor

def main():
    arr = map(int,raw_input().split(","))
    decoupled(arr)

main()
