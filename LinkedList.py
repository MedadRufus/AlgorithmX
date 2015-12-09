





class Node(object):
 
    def __init__(self, data=None, head=None, left=None, right=None, up=None, down=None):
        self.data = data
        self.head = head
        self.left = left
        self.right = right
        self.up = up
        self.down = down



class Header(Node):
    size = 0


def createRoot():
    root = Node()
    root.left = root
    node.right = root
    return root

def createHeader(root):
    header = Header()
    header.right = root
    header.left = root.left
    header.right.left = head
    header.left.right = head
    header.up = head
    header.down = head
    header.size = 0
    return header

def createNode(last, head):
    newnode = Node()
    if last is not None:
        node.left = last
        node.right = last.right
        newnode.left.right = newnode
        newnode.right.left = newnode
    else:
        newnode.left = newnode
        newnode.right = newnode
    newnode.head = head
    head.size += 1
    newnode.down = head
    newnode.up = head.up
    newnode.up.down = newnode
    newnode.down.up = newnode
    return newnode







class DoublyLinkedList(object):
 
    head = None
    tail = None

    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
 
    def remove(self, node_value):
        current_node = self.head
 
        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None
 
            current_node = current_node.next
 
 