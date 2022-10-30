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
    def delete(self,data):
        if(self.key==None):
            print("empty")
            return
        if(self.key>data):
            if(self.lchild):
                self.lchild=self.lchild.delete(data)
            else:
                print("not present")
        elif(self.key<data):
            if(self.rchild):
                self.rchild=self.rchild.delete(data)
            else:
                print("not there")
        else:
            if(self.lchild==None):
                temp=self.rchild
                self=None
                return temp
            if(self.rchild==None):
                temp=self.lchild
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node)
        return self
    
            
            
            
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
root.delete(10)
print("after deleting")
root.postorder()
