from dataclasses import dataclass
import json
from logging import root
from numpy import isin
import zss
from collections import defaultdict
from treelib import Node, Tree


try:
    from editdist import distance as strdist
except ImportError:
    def strdist(a, b):
        if a==b:
            return 0
        else:
            return 1

with open("./Jsonfile/email.json", 'r') as A:
    A_dict = json.load(A)
    # print(type(A_dict[0]["params"]))

with open("./Jsonfile/index.json", 'r') as B:
    B_dict = json.load(B)



id_num = -1

def build_tree(object, Tree, Parent):
    global id_num
    if isinstance(object, list):
        for ob in object:
            build_tree(ob, Tree, Parent)
    elif isinstance(object, dict):
        id_num+=1
        Tree.create_node(object["nodeType"], object["nodeType"]+str(id_num), parent = Parent)
        Parent = object["nodeType"]+str(id_num)
        origin_parent = Parent
        for key, value in object.items():
            if key in ['nodeType', 'name', 'attributes', 'comments', 'attrGroups']:
                continue
            else:
                if isinstance(value, list) or isinstance(value, dict):
                    id_num+=1
                    Tree.create_node(key, key+str(id_num), parent=origin_parent)
                    Parent = key+str(id_num)
                    build_tree(value, Tree, Parent)
    # else:
    #     Tree.create_node(object, str(object)+str(n), Parent)

# class Node(Tree):
#     @staticmethod
#     def get_children(node):
#         # print(node)
#         global treeA
#         return treeA.children("root")
#     @staticmethod
#     def get_tag(tree, node):
#         return Tree.get_node(node.identifier).tag

treeA = Tree()
treeA.create_node("Root", "root")
build_tree(A_dict, treeA, "root")
# treeA.show()
# print(treeA.leaves("root"))
# print(treeA.paths_to_leaves())

treeB = Tree()
treeB.create_node("Root", "root")
build_tree(B_dict, treeB, "root")
treeB.show()
# print(treeB.paths_to_leaves())
# print(treeB.children("Stmt_Function13"))
# print(treeB.get_node("root").tag)
# print(treeB.save2file("treefile"))

# def get_children(node):
#     id_ = treeA.get_node(node.identifier)
#     return treeA.children(id_)

# dist = zss.simple_distance(treeA, treeB, Node.get_children, Node.get_tag)
# print(dist)
# assert dist == 20


