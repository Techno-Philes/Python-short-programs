class BST:
    def __init__(self,key):
        self.key=key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if(self.key==None):
            self.key=data
            return
        if(self.key>data):
            if(self.lchild):
                self.lchild.insert(data)
            else:
                self.lchild=BST(data)
        else:
            if(self.rchild):
                self.rchild.insert(data)
            else:
                self.rchild=BST(data)

    def search(self,data):
        if(self.key==data):
            print("found")
            return
        if(self.key>data):
            if(self.lchild):
                self.lchild.search(data)
            else:
                print("not there")
        else:
            if(self.rchild):
                self.rchild.search(data)
            else:
                print("not found")
    def preorder(self):
        
        print(self.key)
        if(self.lchild):
            self.lchild.preorder()
        if(self.rchild):
            self.rchild.preorder()
    def inorder(self):
        if(self.lchild):
            self.lchild.inorder()
        print(self.key)
        if(self.rchild):
            self.rchild.inorder()
    def postorder(self):
        if(self.lchild):
            self.lchild.postorder()
        if(self.rchild):
            self.rchild.postorder()
        print(self.key)
    def minnode(self):
        current=self
        while(current.lchild):
            current=current.lchild
        print("smallest is",current.key)
        
    def maxnode(self):
        abc=self
        while(abc.rchild):
            abc=abc.rchild
        print("largest is",abc.key)    
root=BST(10)
list1=[39,45,22,9,5,4,88]
for i in list1:
    root.insert(i)
root.search(9)
root.search(69)
print("pre order:")
root.preorder()
print("inorder")
root.inorder()
print("post order")
root.postorder()
root.minnode()
root.maxnode()
