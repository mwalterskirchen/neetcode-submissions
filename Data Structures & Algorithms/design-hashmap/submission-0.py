class MyListNode:
    def __init__(self, key = -1, value = -1, next=None) -> None:
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 10000
        self.data = [MyListNode(-1, -1) for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        cur = self.data[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = MyListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.data[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.value
            cur = cur.next
        
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.data[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def hash(self, key: int) -> int:
        return key % self.size


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
