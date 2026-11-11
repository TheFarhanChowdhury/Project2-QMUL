from TreePrinter import print_tree
from TreeNode import TreeNode
from BST import BST

class BinarySearchTree:

    def __init__(self):
        self.root=None

    def insert(self,key,value=None):
        if self.root is None:
            self.root=TreeNode(key,value)
            return

        node=self.root
        parent=None

        while node is not None:
            parent=node
            if key==node.key:
                node.value=value
            elif key<node.key:
                node=node.left
            else:
                node=node.right

        if key<parent.key:
            parent.left=TreeNode(key,value)
        else:
            parent.right=TreeNode(key,value)

    def search(self,key):
        node=self.root
        while node is not None:
            if key==node.key:
                return node
            elif key<node.key:
                node=node.left
            else:
                node=node.right
        raise KeyError

    def get_value(self,key):
        node=self.root
        while node is not None:
            if key==node.key:
                return node.value
            elif key < node.key:
                node=node.left
            else:
                node=node.right
        raise KeyError

    def delete(self,key):
        node=self.root
        parent=None

        while node is not None and key != node.key:
            parent=node
            if key<node.key:
                node=node.left
            else:
                node=node.right

        if node is None:
            raise KeyError

        if node.left is None and node.right is None:
            if parent is None:
                self.root=None
            elif parent.left==node:
                parent.left=None
            else:
                parent.right=None
        elif node.left is None or node.right is None:
            child=node.left if node.left else node.right
            if parent is None:
                self.root=child
            elif parent.left==node:
                parent.left=child
            else:
                parent.right=child
        else:
            successor_parent=node
            successor=node.right
            while successor.left is not None:
                successor_parent=successor
                successor=successor.left
            node.key = successor.key
            node.value = successor.value
            if successor_parent.left==successor:
                successor_parent.left=successor.right
            else:
                successor_parent.right=successor.right
