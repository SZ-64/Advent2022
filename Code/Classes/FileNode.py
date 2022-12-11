class FileNode:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
    
    def __str__(self):
        return f"{self.name}({self.get_dir_size()})"
    
    __repr__ = __str__

    def add_child(self, node):
        self.children.append(node)
    
    def get_dir_size(self):
        if len(self.children) == 0:
            return self.size
        else:
            return sum([f.get_dir_size() for f in self.children])
    
    def find_by_name(self, target):
        for child in self.children:
            if child.name == target:
                return child