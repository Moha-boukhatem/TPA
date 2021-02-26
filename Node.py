class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None
        self.parent = None

    def insert (self,data):
        if data < self.data :   
            if self.left == None :
                self.left = Node(data)
                self.left.parent = self
            else : 
                self.left.insert(data)


        if data > self.data :         
            if self.right == None :
                self.right = Node(data)
                self.right.parent = self
            
            else : self.right.insert(data)
    
    def get_Node(self,data) :

        if data < self.data :
            return self.left.get_Node(date) if self.left else None
    
        elif data > self.data : 
            return self.right.get_Node(date) if self.right else None
        else :
            return self

    def min(self) : 
        node = self
        while node.left :
            node = node.left
        return node
    
    def max(self) :
        node = self
        while node.right:
            node = node.right
        return node

    def count_children (self) : 

        return bool(self.right) + bool(self.left)

    def plus_petit_plus_grand (self,data) :
        node = self.right
        node.min()
          
    def print(self) :
        tree ="" 
        if self.left or self.right :   
            tree += str(self) 
            return 
        
        return self



root = Node(8)

while i != 0 and i in range(int) :
        
    root.insert(i)



        



    