class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

def get_intersection_node(head1, head2):
    if not head1 or not head2 :
        return None

    p1 = head1
    p2 = head2

    while p1 is not p2:
        p1 = head2 if p1 is None else p1.next
        p2 = head1 if p2 is None else p2.next

    return p1 

node_common = Node(5)
node_common.next = Node(6)

head1 = Node(1)
head1.next = Node(2)
head1.next.next = node_common

head2 = Node(3)
head2.next = Node(4)
head2.next.next = node_common

res = get_intersection_node(head1, head2)
print(f"Intersection node: {res.data if res else None}")

