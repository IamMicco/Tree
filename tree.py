class Branch:

    def __init__(self):
        self.first = None
        self.second = None
        self.third = None
        self.value = self.generate_branch() 
        self.data = self.generate_leaf()

    def generate_branch(self):
        from random import randint
        branch = randint(0,3)
        return branch

    def generate_leaf(self):
        from random import randint
        leaf = randint(0,50)
        return leaf

class Tree:
    def __init__(self):
        self.stem = None

    def create(self):
        self.stem = Branch()
        return self._create(self.stem)

    def _create(self, cur_branch):
        if cur_branch.value != 0:
            if cur_branch.value == 1:
                cur_branch.first = Branch()
                self._create(cur_branch.first)
            elif cur_branch.value == 2:
                cur_branch.first = Branch()
                cur_branch.second = Branch()
                self._create(cur_branch.first)
                self._create(cur_branch.second)
            elif cur_branch.value == 3:
                cur_branch.first = Branch()
                cur_branch.second = Branch()
                cur_branch.third = Branch()
                self._create(cur_branch.first)
                self._create(cur_branch.second)
                self._create(cur_branch.third)

    def add(self):
        if self.stem == None:
            return None
        else:
            return self._add(self.stem)

    def _add(self, cur_node, leaf = 0):
        if cur_node.value == 0:
            leaf += cur_node.data
            return leaf
        elif cur_node.value == 1:
            leaf += cur_node.data
            num_of_leaves = self._add(cur_node.first, leaf)
        elif cur_node.value == 2:
            leaf += cur_node.data
            index = leaf - cur_node.data
            num_of_leaves = self._add(cur_node.first, leaf) + self._add(cur_node.second, index)
        elif cur_node.value == 3:
            leaf += cur_node.data
            index = leaf - cur_node.data
            num_of_leaves = self._add(cur_node.first, leaf) + self._add(cur_node.second, index) + self._add(cur_node.third, index)
        return num_of_leaves

tree = Tree()
tree.create()
print (f'The number of leaves are {tree.add()}')