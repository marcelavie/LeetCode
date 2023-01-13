/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    let list = new Array(nums.length)
    list[0] = nums[0]
    for(let i =1; i < nums.length; i++) {
        list[i] = list[i-1] + nums[i];
    }
    return list;
};
// link: https://leetcode.com/problems/running-sum-of-1d-array/description/