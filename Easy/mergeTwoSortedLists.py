class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0) #head falsa só pra auxiliar o processo
        current = dummy

        while list1 and list2: #percorrer as duas listas ao mesmo tempo faz mais sentido, avançando naquela com menor valor
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        
        return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.val, end=" -> ")
    currentNode = currentNode.next
  print("null")

list1 = create_linked_list([1,2,4,5])
list2 = create_linked_list([2,3,4])
result = Solution().mergeTwoLists(list1, list2)
traverseAndPrint(result)
