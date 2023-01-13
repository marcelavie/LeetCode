/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let integers = {};
    for (let [index, num] of nums.entries()) {
        if(integers[num] !== undefined) return [integers[num], index];
        integers[target-num] = index;
    }
};
// Link: https://leetcode.com/problems/two-sum/