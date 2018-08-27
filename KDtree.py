import sys

class KdNode(object):
    def __init__(self, dom_elt, split, left, right):
        self.dom_elt = dom_elt 
        self.split = split   
        self.left = left    
        self.right = right 

class KdTree(object):
    def __init__(self, data):
        k = len(data[0]) 

        def CreateNode(split, data_set):
            if not data_set:  
                return None
            data_set.sort(key=lambda x: x[split])
            split_pos = len(data_set) // 2   
            median = data_set[split_pos]       
            split_next = (split + 1) % k    # cycle coordinates 
            if split_next == 0:
                split_next += 1
            return KdNode(median, split, CreateNode(split_next, data_set[:split_pos]), CreateNode(split_next, data_set[split_pos + 1:]))                
        self.root = CreateNode(1, data)
            
def preorder(root): 
    print(root.dom_elt) 
    if root.left:   
        preorder(root.left) 
    if root.right: 
        preorder(root.right) 

if __name__ == "__main__":
    data = []
    with open("districtTW.csv") as csv:
        for line in csv:
            lineSplit = line.split(',')
            data.append([lineSplit[3][:-1], lineSplit[1], lineSplit[2]])
    kd = KdTree(data)
    preorder(kd.root)