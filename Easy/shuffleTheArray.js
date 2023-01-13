/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    const list = new Array(2*n); 
    for (let i = 0; i < n; i++) {
        list[2*i] = nums[i];
        list[2*i+1] = nums[n+i];
   } 
   return list
};

// link: https://leetcode.com/problems/shuffle-the-array/submissions/877552843/