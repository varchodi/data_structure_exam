#in a queue the first in is the first out .../.

#student Node class
class Student:
    def __init__(self,name:str) -> None:
        self.name=name
        self.next:Student=None
        self.prev:Student=None

#queue class
class StudentQueue:
    size:int
    def __init__(self) -> None:
        self.size=0
        self.head=None
        self.tail=None # use to facilitate the enqueue and dequeue methods by avoiding loops \

    # student join the que
    def enqueue(self,name:str)->None:
        studentNode=Student(name)
        if(self.is_empty_queue()):
           self.head=self.tail=studentNode
        else :
            studentNode.prev=self.tail
            self.tail.next=studentNode
            self.tail=studentNode
        self.size+=1
        print(f"{name} joined the queue")


    #student quit the queue
    def dequeue(self)->str:
        if(self.is_empty_queue()):
            print("Queue is empty , no one can quit")
        elif(self.size==1):
            head=self.head
            self.head=self.tail=None
            self.size-=1
            print(f"{head.name} has been served")
            return head.name
        else:
            head=self.head
            self.head.next.prev=None
            self.head=self.head.next
            self.size-=1
            print(f"{head.name} served, and quit the queue")
            return head.name



    #check if the que is empty
    def is_empty_queue(self)->bool:
        if(self.head is None and self.size==0):
            print("the queue is empty")
            return True
        else:
            print("there is same guys there")
            return False
        
    #print out students on the queue
    def get_students(self)->None:
        count=1
        if(self.is_empty_queue()):
            print("Sorry, Noone still there")
        else:
            head:Student=self.head
            while(head):
                print(f"{count}. {head.name}")
                head=head.next
                count+=1

    #get the queue size
    def get_size(self)->int:
        print(f"size: {self.size}")
        return self.size
        

line=StudentQueue()

line.get_students()
is_empty=line.is_empty_queue()
line.dequeue()
line.enqueue("green")
line.enqueue("varcho")
is_empty=line.is_empty_queue()
line.get_size()
line.get_students()
line.dequeue()
line.get_size()
line.enqueue("robert")
line.get_size()
line.get_students()