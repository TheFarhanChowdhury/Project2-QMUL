from Node import Node

class TreeNode(Node):
    """A new character class called TreeNode"""
    def __init__(self,key=None,value=None):
        """
        Creating the tree's attributes
        Args:
            key: the place of the node
            value: what is stored
        """
        self._key=key
        self._left=None
        self._right=None
        self._parent=None
        self._value=value


    @property
    def key(self):
        """
        Key is the value of the node
        return: the initialised key
        """
        return self._key

    @key.setter
    def key(self,value):
        self._key=value

    @property
    def left(self):
        """
        The left child of the Node
        return: the value of the left child
        """
        return self._left

    @left.setter
    def left(self,node):
        """
        A method that sets the value of the left child
        Args:
            node: the parent of the left child
        """
        if node is not None and not isinstance(node,TreeNode):
            raise TypeError
        if self._left is not None:
            self._left._parent=None

        self._left=node
        if node is not None:
            node._parent=self

    @property
    def right(self):
        """
        The right child of the Node
        return: the value of the right child
        """
        return self._right

    @right.setter
    def right(self, node):
        """
        A method that sets the value of the right child
        Args:
            node: the parent of the right child being set
        """
        if node is not None and not isinstance(node,TreeNode):
            raise TypeError

        if self._right is not None:
            self._right._parent = None

        self._right = node
        if node is not None:
            node._parent = self

    @property
    def parent(self):
        """
        The parent of the node
        Returns: the parent
        """
        return self._parent

    @parent.setter
    def parent(self, value):
        """
        A method that returns the value of the parent of the node
        Args:
            value: the value of the parent
        """
        self._parent = value

    @property
    def value(self):
        """
        The value of the node
        """
        return self._value

    @value.setter
    def value(self,value):
        self._value=value

    @property
    def depth(self):
        depth=1
        current_node=self
        while current_node.parent is not None:
            depth+=1
            current_node=current_node.parent
        return depth

    def remove_leaf(self,n):
        """
        A method that removes a leaf from the binary tree
        Args:
            n: the node being deleted
        Returns: the node being deleted
        """
        if not isinstance(n,TreeNode):
            raise TypeError
        elif n.left is not None or n.right is not None:
            raise ValueError
        elif self.left==n:
            self.left=None
        elif self.right==n:
            self.right=None
        else:
            raise ValueError
        return n

    def __repr__(self):
        if self.parent is not None:
            parent_key=self.parent.key
        else:
            parent_key=None

        return f"TreeNode(key={self.key}, left={self.left}, right={self.right}, parent={parent_key})"



