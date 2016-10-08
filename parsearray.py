def main():
    n = int(raw_input())

    string = []
    for i in range(n):
        string.append(raw_input())

    q = int(raw_input())

    queries = []
    for i in range(q):
        queries.append(raw_input())

    for query in queries:
        findString(string,query)

def findString(string,query):
    count = 0
    for str1 in string:
        if str1 == query:
            count = count + 1

    print count

main()
