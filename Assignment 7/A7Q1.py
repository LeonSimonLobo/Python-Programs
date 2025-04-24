class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_List:
    def __init__(self):
        self.head=None
    def insertNode(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=Node(data)
    def deleteNode(self,value):
        if self.head==None:
            print("Linked List is empty.")
            return
        if self.head.data==value:
            self.head=None
            return
        temp=self.head
        while temp is not None:
            if temp.data==value:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            print("Position is not in Linked List.")
            return
        else:
            prev.next=temp.next
    def displayLinkedList(self):
        if self.head==None:
            print("Linked List is empty.")
        temp=self.head
        while temp!=None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")
def menu():
    print("\nEnter 'insert' to insert a new node")
    print("Enter 'delete' to delete a specific node")
    print("Enter 'display' to display linked list")
    choice=input("Enter 'exit' to exit:")
    return choice
def main():
    choice=menu()
    LL=Linked_List()
    while choice!='exit':
        if choice=='insert':
            LL.insertNode(int(input("Enter value:")))
        elif choice=='delete':
            LL.deleteNode(int(input("Enter value:")))
        else:
            LL.displayLinkedList()
        choice=menu()
if __name__=='__main__':
    main()