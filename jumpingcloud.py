def main():
    n = int(raw_input().strip())
    c = map(int,raw_input().strip().split(' '))
    print jumpingCloud(n,c,0,0)

def jumpingCloud(n,c,i,j):

    if(i==n-1):
        return j

    elif (i>=n-1 or c[i]==1):
        return -1

    k = jumpingCloud(n,c,i+2,j+1)
    return jumpingCloud(n,c,i+1,j+1) if  k == -1 else k

main()
