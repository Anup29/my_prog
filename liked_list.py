class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

head = n1
current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print()
print("*" * 50)

# new node at begining
head = n1
new_node = Node(40)
new_node.next = head
head = new_node
current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print()
print("*" * 50)

# Delete 1st node
if head.next is not None:
    head = head.next
current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print()
print("*" * 50)

#Delete from end
current = head
while current.next.next is not None:
    current = current.next
current.next = None
current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print()
print("*" * 50)

#Delete speicif element
current = head
while current.next.data != 20:
    current = current.next
current.next = current.next.next

current = head
while current is not None:
    print(current.data,end="->")
    current = current.next
print()
print("*" * 50)