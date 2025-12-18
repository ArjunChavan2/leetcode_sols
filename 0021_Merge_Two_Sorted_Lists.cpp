struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1) return list2;
        if (!list2) return list1;

        if (list1->val <= list2->val) {
            list1->next = mergeTwoLists(list1->next, list2);
            return list1;
        } else {
            list2->next = mergeTwoLists(list1, list2->next);
            return list2;
        }
    }
};

/* This solution has a time complexity of O(n + m), where n and m are the lengths of the two inputted lists.
This algorithm is efficient because it merges the two lists recursively by add the smaller node to
the function call of the next of that list and the other list. This continues until one of the lists is empty,
at which point the remaining nodes of the other list are appended to the merged list.
*/