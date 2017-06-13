#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    counter = 0
    lnode = None
    
    while True:
        print 'test'
        if not lnode:
            lnode = ListNode(l1.val + l2.val)
        else:
            lnode.next = ListNode(l1.val + l2.val)                   
        
        print lnode.val
        lnode = lnode.next
        l1 = l1.next
        l2 = l2.next
        if l1 is None:
            break
    
    return lnode


input1 = [3,4,2]
input2 = [4,6,5]

l1 = None
l2 = None
for i in input1:
    if l1 is None:
        l1 = ListNode(i)
    else:
        l1.next = ListNode(i)
        l1 = l1.next

for i in input2:
    if l2 is None:
        l2 = ListNode(i)
    else:
        l2.next = ListNode(i)
        l2 = l2.next



v = addTwoNumbers(l1, l2)

while True:
    print v.val
    if v is None:
        break
    else:
        v = v.next

