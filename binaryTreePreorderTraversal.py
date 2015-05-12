ass Solution:
    # @param root, a tree node
    # @return a list of integers
    def iterative_preorder(self, root, list):
        stack = []
        while root or stack:
            if root:
                list.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return list

    def preorderTraversal(self,root):
        list = []
        self.iterative_preorder(root,list)
        return list


