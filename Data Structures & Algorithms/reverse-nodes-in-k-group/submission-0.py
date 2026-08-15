# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_list_k(self, head, k):
        tmp = head
        prev = None
        nxt = tmp.next

        for i in range(k):
            tmp.next = prev
            prev = tmp
            tmp = nxt
            if tmp:
                nxt = tmp.next
        
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #traverse the whole list to get length in len_
        len_ = 0
        tmp = head
        while(tmp):
            tmp = tmp.next
            len_ += 1

        if len_ < k:
            return head
        
        prev_grp_last = None
        cur_grp_first = head
        next_grp_first = None

        while(1):
            less_than_k_inlist = False
            #get next_grp_first
            tmp = cur_grp_first
            for i in range(k):
                if (tmp):
                    tmp = tmp.next
                else:
                    #less than k elements left in the list
                    less_than_k_inlist = True
                    break
            
            if less_than_k_inlist:
                prev_grp_last.next = cur_grp_first
                break
            else:
                next_grp_first = tmp

            tmp = self.reverse_list_k(cur_grp_first, k)

            if prev_grp_last == None:
                head = tmp
            else:
                prev_grp_last.next = tmp

            prev_grp_last = cur_grp_first
            cur_grp_first = next_grp_first

        return head