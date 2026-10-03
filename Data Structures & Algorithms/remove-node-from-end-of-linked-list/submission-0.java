/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        int size = 0;

        while (curr != null) {
            curr = curr.next;
            size ++;
        }

        // Edge cases:
        //      - n = size, (so head is being removed)
        //      - n = 1, (so tail is being removed)
        //      - 1 < n < size, (so a middle node is being removed)
        //      - size = 1, (only node being removed)


        int nth = size - n; // Gives you the (0-indexed) index of node to remove 
        
        if (nth == 0) {
            return head.next;
        } 

        int i = 0;
        curr = head;
        ListNode next = curr.next;

        while (i < nth-1) {
            curr = curr.next;
            next = next.next;
            i++;
        }

        curr.next = next.next;

        return head;
    }
}
