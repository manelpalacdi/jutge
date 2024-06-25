# Write a backtracking program to print all the combinations of z zeros and o ones 
# such that z + o = n, for a given n.

class Tree:
    def __init__(self, x) -> None:
        self.v = x
        self.childs = []
    def add_child(self, t):
        self.childs.append(t)

def zeros_n_ones(n):
    i = 0
    t0 = Tree(0)
    t1 = Tree(1)
    # create tree for root starting in 0 and root starting in 1
    create_tree(t0, 1, n)
    create_tree(t1, 1, n)
    # print all branches from root
    print_branches(t0)
    print_branches(t1)

def create_tree(t: Tree, current_depth, max_depth):
    if current_depth < max_depth:
        t.add_child(Tree(0))
        t.add_child(Tree(1))
        create_tree(t.childs[0], current_depth + 1, max_depth)
        create_tree(t.childs[1], current_depth + 1, max_depth)

stk = []
def print_branches(t: Tree):
    # add value to stack
    stk.append(t.v)
    # if we got to the end, print and rv last value
    if (len(t.childs) == 0):
        print(" ".join(map(str, stk)))
        stk.pop()
        return
    for child in t.childs:
        print_branches(child)
    # if we ended searching all childs of node, rv last value and go back
    stk.pop()
    return

if __name__ == "__main__":
    zeros_n_ones(3)