class Node:
        def __init__(self,data):
                self.data=data
                self.nref=None
                self.pref=None

class doublyLL:
        def __init__(self):
                self.head=None
        def printLL(self):
                if(self.head==None):
                        print("empty")
                else:
                        n=self.head
                        while(n!=None):
                                print(n.data)
                                n=n.nref
        def printLL_back(self):
                if(self.head==None):
                        print("empty")
                else:
                        n=self.head
                        while(n.nref!=None):
                                n=n.nref
                        while(n!=None):
                                print(n.data)
                                n=n.pref
        def insert_empty(self,data):
                if(self.head==None):
                        new_node=Node(data)
                        self.head=new_node
                else:
                        print("nonsense")
        def add_begin(self,data):
                new_node=Node(data)
                if(self.head==None):
                        self.head=new_node
                else:
                        new_node.nref=self.head
                        self.head.pref=new_node
                        self.head=new_node
        def add_end(self,data):
                new_node=Node(data)
                if(self.head==None):
                        self.head=new_node
                else:
                        n=self.head
                        while(n.nref!=None):
                                n=n.nref
                        n.nref=new_node
                        new_node.pref=n
        def delete_begin(self):
            if(self.head==None):
                print("empty list")
                return
            if(self.head.nref==None):
                self.head=None
                print("now it became empty")
            else:
                self.head=self.head.nref
                self.head.pref=None
        def delete_end(self):
            if(self.head==None):
                print("empty list")
                return
            if(self.head.nref==None):
                self.head=None
                print("now it became empty")
            else:
                n=self.head
                while(n.nref!=None):
                    n=n.nref
                n.pref.nref=None
        def del_byval(self,x):
            if(self.head==None):
                print("empty list")
                return
            if(self.head.nref==None):
                if(x==self.head.data):
                    self.head=None
                    print("now it became empty")
                else:
                    print("x is not present")
                return
            if(self.head.data==x):
                self.head=self.head.nref
                self.head.pref=None
                return
            n=self.head
            while(n.nref!=None):
                if(x==n.data):
                    break
                n=n.nref
                if(n.nref!=None):
                    n.nref.pref=n.pref
                    n.pref.nref=n.nref
                    
                else:
                    if(n.data==x):
                        n.pref.nref=None
                    else:
                        print("x is not present")
            
                                
dl1=doublyLL()
dl1.insert_empty(50)
dl1.add_begin(80)
dl1.add_begin(5)
dl1.add_end(8)
dl1.delete_begin()
dl1.delete_end()
dl1.del_byval(8)
dl1.printLL()


