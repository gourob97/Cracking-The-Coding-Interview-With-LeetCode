my_list = [8,3,10,1,6,14,4,7,13]


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None



root = None

for item in my_list: 
	if root is None:
		root = Node(item)

	else:
		temp = root
		prev = root

		while temp:
			if item < temp.data:
				prev = temp
				temp = temp.left
			else:
				prev = temp
				temp = temp.right

		if item < prev.data:
			prev.left = Node(item)
		else:
			prev.right = Node(item)






print(root.