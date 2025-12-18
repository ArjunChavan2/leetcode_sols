#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* root = new ListNode();
        ListNode* iter = root;
        int carry = 0;
        while(l1 != nullptr && l2 != nullptr)
        {
            ListNode* newNode = new ListNode();
            newNode->val = l1->val + l2->val + carry;
            std::cout << newNode->val << std::endl;
            if (newNode->val >= 10)
            {
                carry = newNode->val / 10;
                newNode->val = newNode->val % 10;
            }
            else
                carry = 0;
            
            iter->next = newNode;
            iter = iter->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1 != nullptr)
        {
            ListNode* newNode = new ListNode();
            newNode->val = l1->val + carry;
            std::cout << newNode->val << std::endl;
            if (newNode->val >= 10)
            {
                carry = newNode->val / 10;
                newNode->val = newNode->val % 10;
            }
            else
                carry = 0;
            
            iter->next = newNode;
            iter = iter->next;
            l1 = l1->next;
        }
        while(l2 != nullptr)
        {
            ListNode* newNode = new ListNode();
            newNode->val = l2->val + carry;
            std::cout << newNode->val << std::endl;
            if (newNode->val >= 10)
            {
                carry = newNode->val / 10;
                newNode->val = newNode->val % 10;
            }
            else
                carry = 0;
            
            iter->next = newNode;
            iter = iter->next;
            l2 = l2->next;
        }

        if(carry > 0)
        {
            ListNode* newNode = new ListNode();
            newNode->val = carry;
            iter->next = newNode;
        }

        return root->next;
    }
};


/* This is a C++ implementation of the Add Two Numbers problem.
   It defines a ListNode structure to represent each node in the linked list.
   The addTwoNumbers function takes two linked lists (l1 and l2) as input,
   which represent two non-negative integers in reverse order. It adds the two numbers
   and returns the sum as a new linked list in the same reverse order format.

   The function iterates through both linked lists, adding corresponding digits along with any carry from the previous addition.
   If one list is longer than the other, it continues adding the remaining digits of the longer list.
   Finally, if there is any carry left after processing both lists, it adds a new node with the carry value.

   The time complexity of this solution is O(max(m, n)), where m and n are the lengths of the two input linked lists.
*/