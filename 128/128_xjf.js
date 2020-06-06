/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length == 0) return 0;
    let min = 0, a = [];
    for (let n of nums) min = Math.min(min, n);
    for (let n of nums) a[n - min] = n;
    let last = -NaN, cur = 0, res = 1;
    for (let n in a) {
        n = a[n];
        if (n == last + 1) res = Math.max(res, ++cur);
        else cur = 1;
        last = n;
    }
    return res;
};