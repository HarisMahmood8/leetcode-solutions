/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    var first = m - 1;
    var second = n - 1;
    all = m + n - 1;
    while(second >= 0) {
        if(nums1[first] > nums2[second]) {
            nums1[all] = nums1[first];
            all--;
            first--;
        }
        else {
            nums1[all] = nums2[second];
            all--;
            second--;
        }
    }
  
  };
