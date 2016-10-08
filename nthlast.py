class linkedlist(object):
    def __init__(self):
        self.head = None

    class node(object):

        def __init__(self,data):
            self.val = data
            self.next = None

    def push(self,val):
        new_node = self.node(val)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        tnode = self.head
        while tnode != None:
            print tnode.val
            tnode = tnode.next

    def printnthnode(self,n):
        tnode = self.head
        while tnode != None and n>1:
            n = n - 1
            tnode = tnode.next

        print tnode.val


def main():
    linklist = linkedlist()
    N = int(raw_input())
    arr = raw_input().split()
    if N > len(arr):
        print "NIL"
        return

    for ele in arr:
        linklist.push(ele)

    linklist.printnthnode(N)

main()
