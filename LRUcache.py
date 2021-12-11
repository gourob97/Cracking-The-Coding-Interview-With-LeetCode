class Node:
	def __init__(self, kv=(0,0), prev=None,next= None):
		self.kv = kv
		self.prev = prev
		self.next = next 



class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mydict = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next =  self.tail
        self.tail.prev = self.head

    	
    def get(self, key: int) -> int:
        if key in self.mydict.keys():
            node = self.mydict[key]
            before = node.prev
            after = node.next
            before.next = after
            after.prev = before
            temp = self.head.next
            temp.prev = node
            node.prev = self.head
            node.next = temp
            self.head.next = node
            return self.mydict[key].kv[1]
        else:
            return -1
    
    
    def put(self, key: int, value: int) -> None:
        if key in self.mydict.keys():
            node = self.mydict[key]
            before = node.prev
            after = node.next
            before.next = after
            after.prev = before
            del self.mydict[key]




        if len(self.mydict) == self.capacity:
            del self.mydict[self.tail.prev.kv[0]]
            node = self.tail.prev.prev
            node.next = self.tail
            self.tail.prev = node



        if key not in self.mydict.keys():
            before = self.head
            after = self.head.next
            node = Node((key,value))
            node.prev = before
            node.next = after
            before.next = node
            after.prev = node
            self.mydict[key] = node
            return None
        


        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)





