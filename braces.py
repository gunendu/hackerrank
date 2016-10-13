def main():
    n = int(raw_input())
    for i in range(n):
        stack = []
        value = raw_input()
        value = list(value)
        flag = True
        i = 0
        while(i<len(value)):
            if value[i] in ['{','[','(']:
                stack.append(value[i])
            else:
                if(len(stack)>0):
                    temp = stack.pop()
                    if temp is '(' and value[i] is ')' or temp is '{' and value[i] is '}' or temp is'[' and value[i] is ']':
                        pass
                    else:
                        flag = False
                else:
                    flag = False
            i = i + 1

        if len(stack) > 0:
            flag = False

        if(flag):
            print "YES"
        else:
            print "NO"

main()
