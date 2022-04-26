import json
import networkx as nx
from numpy import isin
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import matplotlib 
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import zss
from apted import APTED, Config

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.children = []
    
    def get_num_nodes(self):
        return 1 + sum(map(lambda child: child.get_num_nodes(), self.children))
        

    # def save_plot(self):
    #     G=nx.Graph()
    #     label_dict = {}
    #     def traverse(node):
    #         label_dict[node] = node.val
    #         for child in node.children:
    #             G.add_edge(
    #                 node,
    #                 child
    #                 )
    #             traverse(child)
    #     traverse(self)
        
        
    #     pos = graphviz_layout(G, prog="dot")
    #     nx.draw(G, pos, labels=label_dict, with_labels=True)
    #     plt.savefig('result.png')
    
    @staticmethod
    def get_children(node):
        return node.children

    @staticmethod
    def get_label(node):
        return node.name
    

def parse(data):
    if isinstance(data, dict):
        if 'nodeType' in data:
            node = Node(data['nodeType'])
            for key in data:
                if key in ['nodeType', 'name', 'attributes', 'comments', 'attrGroups']:
                    continue
                child = Node(key)
                if isinstance(data[key], list):
                    for element in data[key]:
                        grandchild = parse(element)
                        if grandchild is not None:
                            child.children.append(grandchild)
                elif isinstance(data[key], dict):
                    grandchild = parse(data[key])
                    if grandchild is not None:
                        child.children.append(grandchild)

                if len(child.children) > 0:
                        node.children.append(child)
            return node
        else:
            return None
    elif isinstance(data, list):
        node = Node('root')
        for element in data:
            child = parse(element)
            if child is not None:
                node.children.append(child)
        return node
    else:
        return None

def print_tree(node, prefix=[]):
        space =  '     '
        branch = '│   '
        tee =    '├─ '
        last =   '└─ '

        global tree_plot
        global node_num

        if len(prefix)==0:
            tree_plot = ''
            node_num = 0
        
        tree_plot += ''.join(prefix) + str(node.name) + '\n'
        node_num += 1

        if len(prefix)>0:
            prefix[-1] = branch if prefix[-1] == tee else space
  
        for i, e in enumerate(node.children):
            if i <len(node.children)-1:
                print_tree(e, prefix+ [tee])
            else:
                print_tree(e, prefix+[last])
        
        return tree_plot

        

def build_tree(pathA, pathB):
    with open(pathA) as A:
        A_json = json.load(A)
    with open(pathB) as B:
        B_json = json.load(B)

    treeA = parse(A_json)
    treeB = parse(B_json)

    return treeA, treeB

def compute_zss_distance(pathA, pathB):
    treeA, treeB = build_tree(pathA, pathB)
    dist = zss.simple_distance(treeA, treeB, Node.get_children, Node.get_label)
    # print(dist)
    return dist

def compute_apted_distance(pathA, pathB):
    treeA, treeB = build_tree(pathA, pathB)
    apted = APTED(treeA, treeB)
    ted = apted.compute_edit_distance() 
    # print(treeB.get_num_nodes())
    # print(treeA.get_num_nodes())
    return ted

def test():
    tree_plot = ''
    # with open("/home/yumeng/phishing-research/html_parser/Jsonfile/13.58.156.103_fileee.zip_6cc33ce9c6ba0c949ee3/email.json", 'r') as A:
    #     A_dict = json.load(A)
    # with open("/home/yumeng/phishing-research/html_parser/Jsonfile/template/complex.json", 'r') as B:
    #     B_dict = json.load(B)
    # with open("/home/yumeng/phishing-research/html_parser/Jsonfile/template/index.json", 'r') as A:
    #     A_dict = json.load(A)
    # with open("/home/yumeng/phishing-research/html_parser/Jsonfile/template/email.json", 'r') as B:
    #     B_dict = json.load(B)
    # treeA = parse(A_dict)
    # treeB = parse(B_dict)
    pathA = "/home/yumeng/phishing-research/html_parser/Jsonfile/13.58.156.103_fileee.zip_6cc33ce9c6ba0c949ee3/email.json"
    pathB = "/home/yumeng/phishing-research/html_parser/Jsonfile/template/email.json"

    
    apted_distance = compute_apted_distance(pathA, pathB)
    # zss_distance = compute_zss_distance(treeA, treeB)
    print("apted: ", apted_distance)
    # print("zss: ", zss_distance)

    # print(print_tree(treeB))
    # print(print_tree(treeA))
    # print_tree(treeA)
    

# node_num = 0
# test()
# print(node_num)

