/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    const index  = nums.findIndex((num, i) => num >= target)
    return index >= 0 ? index : nums.length;
};