def main():
    s = raw_input().strip()
    n = long(raw_input().strip())

    count = 0
    for i in range(0,len(s)):
        if s[i] == 'a':
            count = count + 1

    lens = n/len(s)
    mod = n%len(s)

    totalcount = lens*count

    for i in range(0,mod):
        if s[i] == 'a':
            totalcount = totalcount + 1

    print totalcount

main()
