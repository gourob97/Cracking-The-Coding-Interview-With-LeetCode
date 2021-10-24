class Node:
	def __init__(self, data):
		self.data =  data
		self.left = None
		self.right = None

	def insert(self, data):
		#if the data already exist

		if data == self.data:
			return

		if data < self.data:
			#insert in left subtree
			if self.left:
				self.left.insert(data)
			else:
				self.left = Node(data)

		else:
			#insert in right subtree
			if self.right:
				self.right.insert(data)
			else:
				self.right = Node(data)

		

my_list = [8,3,10,1,6,14,4,7,13]

root = None

for item in my_list:
	if root is None:
		root = Node(item)
	else:
		root.insert(item)




