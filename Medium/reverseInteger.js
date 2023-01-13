/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    if(x < 0) return -1 * reverse(-x);
    const conversor = (x+'').split('').reverse().join('');
    return (conversor > 2**31 -1) ? 0 : conversor;
};
// link: https://leetcode.com/problems/reverse-integer/description/