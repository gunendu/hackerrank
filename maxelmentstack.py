def main():
    n = int(raw_input())
    stack = []
    maxno = -1
    for i in range(n):
        commands = raw_input().split()
        if commands[0] == '1':
            element = int(commands[1])
            stack.append(element)
            if maxno < element:
                maxno = element
        if commands[0] == '2':
            temp = stack.pop()
            if temp == maxno:
                maxno = -1
                if len(stack) > 0:
                    maxno = max(stack)
        if commands[0] == '3':
            print maxno


main()
