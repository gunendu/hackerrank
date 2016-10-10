def main():
    n = int(raw_input())
    s = ""
    stack = []
    for i in range(n):
        arr = raw_input().split()
        if len(arr)>1:
            ops = arr[0]
            oprnd = arr[1]
        else:
            ops = arr[0]
        if ops is '1':
            stack.append(s)
            s = s + str(oprnd)
        if ops is '3':
            oprnd = int(oprnd)
            print s[oprnd - 1]
        if ops is '2':
            stack.append(s)
            oprnd = int(oprnd)
            s = s[:-(oprnd)]
        if ops is '4':
            s = stack.pop()

main()
