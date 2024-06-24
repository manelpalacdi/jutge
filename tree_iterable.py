class Tree:

    def __init__(self, x) -> None:
        self.rt = x
        self.child = []
        
    def __iter__(self):
        queue = [self]
        while queue:
            node = queue.pop(0)
            yield node.root()
            for child in node.child:
                queue.append(child)

    def add_child(self, a):
        self.child.append(a)

    def root(self):
        return self.rt
    
    def ith_child(self, i: int):
        return self.child[i]
    
    def num_children(self):
        return (len(self.child))
    

if __name__ == "__main__":
    t = Tree(2)
    t.add_child(Tree(3))
    t.add_child(Tree(4))
    t.ith_child(0).add_child(Tree(5))
    print([x for x in t])