function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
  }

// Create l1: [2, 4, 3] 342
var l1 = new ListNode(2);
l1.next = new ListNode(4);
l1.next.next = new ListNode(3);

// Create l2: [5, 6, 4] 465
var l2 = new ListNode(5);
l2.next = new ListNode(6);
l2.next.next = new ListNode(4);

function add_two_numbers(l1, l2) {
    var total_l1 = 0;
    var total_l2 = 0;
    var cur1 = l1;
    var cur2 = l2;
    mult1 = 10;
    mult2 = 10;
    total_l1 += cur1.val;
    total_l2 += cur2.val;

    cur1 = cur1.next;
    cur2 = cur2.next;

    while(cur1 != null) {
        total_l1 += cur1.val * mult1;
        mult1 *= 10;
        cur1 = cur1.next;
    }


    while(cur2 != null) {
        total_l2 += cur2.val * mult2;
        mult2*=10;
        cur2 = cur2.next;
    }
    var x = total_l1 + total_l2
    return x;
};


add_two_numbers(l1, l2);
