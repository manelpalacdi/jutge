class Tree:
    def __init__(self, x) -> None:
        self.rt = x
        self.child = []
    
    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt
    
    def ith_child(self, i: int):
        return self.child[i]
    
    def num_children(self):
        return (len(self.child))
    
class Pre(Tree):
    order = []
    def preorder(self):
        Pre.order.append(self.rt)
        for child in self.child:
            child.preorder()
        return Pre.order

if __name__ == "__main__":
    t = Pre(2)
    t.add_child(Pre(3))
    t.add_child(Pre(4))
    print(t.num_children())
    t.ith_child(1).add_child(Pre(5))
    print(t.preorder())
