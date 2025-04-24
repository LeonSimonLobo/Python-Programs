class Queue:
    def __init__(self):
        self.front=None
        self.tail=None
        self.queue=[]
    def Enqueue(self,value):
        self.queue.append(value)
        if self.front==None:
            self.front=self.queue[0]
        self.tail=self.queue[len(self.queue)-1]
    def Dequeue(self):
        if self.front==None:
            print("Queue is empty.")
            return
        elif self.front==self.tail:
            self.front=None
        else:
            self.front=self.queue[1]
        
        print(self.queue[0],"Dequeued succesfully.")
        return self.queue.pop(0)
def menu():
    print("\nEnter 'add' to enqueue")
    print("Enter 'delete' to dequeue")
    choice=input("Enter 'exit' to exit:")
    return choice
def main():
    choice=menu()
    q=Queue()
    while choice!='exit':
        if choice=='add':
            q.Enqueue(int(input("Enter value:")))
        else:
            q.Dequeue()
        choice=menu()
if __name__=='__main__':
    main()