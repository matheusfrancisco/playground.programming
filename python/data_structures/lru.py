class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU:
    head: Node| None = None
    tail: Node| None = None

    def __init__(self, max_c: int):
        self.head = self.tail = None
        self.capacity = max_c 
        self.length = 0 
        self.lookup = {}
        self.reservese_lookup = {}

    def get(self, key):
        # check the cache for the key
        node = self.lookup.get(key, None)  
        if node is None:
            return None
        self.detach(node) 
        self.preprend(node)
        # update the value we found and move it to the front
        # return out the value found or None if not found
        return node.value

    def detach(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        if self.head is not None and \
            self.head.value == node.value and self.head.key == node.key:
            self.head = self.head.next

        if self.tail is not None and \
            self.tail.value == node.value and self.tail.key == node.key:
            self.tail = self.tail.prev
        node.next = None
        node.prev = None

    def preprend(self, node):
        if self.head is None:
            self.head = self.tail = node
            return

        node.next = self.head
        self.head.prev = node


    def trim_cache(self):
        if self.length <= self.capacity:
            return
        tail = self.tail
        self.detach(tail)
        key = self.reservese_lookup.get(tail, None)
        if key:
            del self.lookup[key]
            del self.reservese_lookup[tail]
            self.length -= 1


    def update(self, key, value):
        # does it exist in the cache?
        # if it doesn't exist, we need to add it to the cache
            # - check capacity and evict if over
        # if it does exist, we need to update the value and move it to the front
        node = self.lookup.get(key, None)  
        if node is None:
            node = Node(key, value)
            self.length += 1
            self.preprend(node)
            self.trim_cache()
            self.lookup[key] = node
            self.reservese_lookup[node] = key
        else:
            self.detach(node)
            self.preprend(node)
            node.value = value

l = LRU(3)
l.update('a', 1)
l.update('b', 1)
print(l.get('a'))
l.update('a', 2)
l.update('c', 2)
l.update('d', 2)
print(l.get('b'))
l.update('a', 2)
l.update('a', 3)
print(l.get('a'))
