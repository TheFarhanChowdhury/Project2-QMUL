from TreeNode import TreeNode

def inorder(node):
    if node is None:
        return []
    return inorder(node.left)+[node.key]+inorder(node.right)

def preorder(node):
    if node is None:
        return []
    return [node.key]+preorder(node.left)+preorder(node.right)

def postorder(node):
    if node is None:
        return []
    return postorder(node.left)+postorder(node.right)+[node.key]