class MinHeap:
	def __init__(self,heapSize):
		self.heapSize=heapSize
		self.MinHeap=[0]*(heapSize+1)
		self.realSize = 0

	def add(self, element):
		self.realSize+=1
		if self.realSize>self.heapSize:
			print("Overflow")
			self.realSize-=1
			return
		self.MinHeap[self.realSize]=element

		index = self.realSize
		parent = index//2

		while index>1 and self.MinHeap[parent]>self.MinHeap[index]:
			self.MinHeap[parent],self.MinHeap[index] = self.MinHeap[index], self.MinHeap[parent]
			index=parent
			parent = index//2

	def top(self):
		return self.MinHeap[1]


	def remove(self):
		if self.realSize<1:
			print("The heap is empty")
			return

		self.MinHeap[1],self.MinHeap[self.realSize]=self.MinHeap[self.realSize],self.MinHeap[1]
		self.realSize-=1

		index = 1


		while index<=self.realSize//2:
			left = index*2
			right = left+1

			if self.MinHeap[index]> self.MinHeap[right] or self.MinHeap[index]> self.MinHeap[left]:
				if self.MinHeap[left]> self.MinHeap[right]:
					self.MinHeap[index],self.MinHeap[right] = self.MinHeap[right],self.MinHeap[index]
					index = right
				else:
					self.MinHeap[index],self.MinHeap[left] = self.MinHeap[left],self.MinHeap[index]
					index = left

			else:
				break







if __name__ == "__main__":
	minheap = MinHeap(6)

	minheap.add(6)
	minheap.add(3)
	minheap.add(15)
	minheap.add(4)
	minheap.add(3)
	minheap.add(2)
	#minheap.remove()
	print(minheap.MinHeap)







