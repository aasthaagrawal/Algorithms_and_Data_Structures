class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def push(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def append(self,data):
        newNode=Node(data)
        tmp=self.head
        while tmp.next:
            tmp=tmp.next
        tmp.next=newNode

    def deleteNode(self,key):
        tmp=self.head
        prev=None
        while tmp:
            if tmp.data==key:
                if prev==None:
                    self.head=tmp.next
                    tmp=None
                    return
                else:
                    prev.next=tmp.next
                    tmp=None
                    return
            prev=tmp
            tmp=tmp.next
        

    def deleteLL(self):
        tmp=self.head
        self.head=None
        while tmp:
            next=tmp.next
            tmp=None
            tmp=next

    def printLL(self):
        tmp=self.head
        while(tmp is not None):
            print(tmp.data)
            tmp=tmp.next

if __name__=='__main__':
    lList=LinkedList()
    lList.push(3)
    lList.push(2)
    lList.push(1)
    lList.append(19)
    lList.printLL()
    print("***")
    lList.deleteNode(19)
    lList.printLL()
