# Definition for a binary tree node.
# class TreeNode(object):
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

class Solution(object):
	def longestConsecutive(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		return self.recursive_no_state(root)
		
        

	def traverse_tree_2(self, root, prev_val=1.1, count=1):
		if not root:
			return count

		if root.val - prev_val == 1:
			return max(self.traverse_tree_2(root.left, root.val, count + 1), self.traverse_tree_2(root.right, root.val, count + 1))
		else:
			return max(count, self.traverse_tree_2(root.left, root.val, 1), self.traverse_tree_2(root.right, root.val, 1))

	def recursive_with_state(self, parent, path=None):
		if not parent:
			return

		if not path:
			path = [parent.val]
			self.max_length = 1
		elif parent.val - path[-1] == 1:
			path.append(parent.val)
			length = len(path)
			if length > self.max_length:
				self.max_length = length
		else:
			path = [parent.val]

		if parent.left:
			self.traverse_tree(parent.left, path[:])
		if parent.right:
			self.traverse_tree(parent.right, path[:])