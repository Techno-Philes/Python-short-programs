class Node:
    def _init_(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def _init_(self):
        self.head=None
    def print_LL(self):
        if self.head==None :
            print("linked list is empty")
        else:
            n=self.head
            while(n!=None):
                
                    print(n.data)
                    n=n.ref
                    
LL1=linkedlist()
LL1.print_LL()
