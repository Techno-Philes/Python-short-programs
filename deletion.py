class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self):
        self.head=None

    def print(self):
        if self.head==None:
            print("empty list")
        else:
            n=self.head
            while(n!=None):
                print(n.data)
                n=n.ref
    def add(self,data):
      new_node=Node(data)
      new_node.ref=self.head
      self.head=new_node
            
                
    def add_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            n=self.head
            while(n.ref!=None):
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while(n!=None):
            if (x==n.data):
                break
            else:
                n=n.ref
        if(n==None):
            print("node is not present")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def add_before(self,data,x):
        if(self.head==None):
            print("empty")
            return
        if(self.head.data==x):
            new_node=Node(data)
            new_node.ref=self.head
            self.head=new_node
            return
        n=self.head
        while(n.ref!=None):
            if(n.ref.data==x):
                break
            n=n.ref
        if(n.ref==None):
            print("not found")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    def delete_begin(self):
        if(self.head==None):
            print("cannot perform anything")
        else:
            self.head=self.head.ref
    
    def delete_end(self):
        if(self.head==None):
            print("cannot perform")
        elif(self.head.ref==None):
            self.head=None
        else:
            n=self.head
            while(n.ref.ref!=None):
                n=n.ref
            n.ref=None    
    def delete_byval(self,x):
        if(self.head==None):
            print("u cant dlt")
            return
        if(x==self.head.data):
            self.head=self.head.ref
            return
        n=self.head
        while(n.ref!=None):
            if(x==n.ref.data):
                break
            n=n.ref
        if(n.ref==None):
            print("node is not pesent")
        else:
            n.ref=n.ref.ref

                    
LL1=Linkedlist()
LL1.add(10)
LL1.add_end(20)
LL1.add(500)
LL1.add_after(26,500)
LL1.add_before(69,10)
LL1.delete_begin()
LL1.delete_byval(10)
LL1.print()
