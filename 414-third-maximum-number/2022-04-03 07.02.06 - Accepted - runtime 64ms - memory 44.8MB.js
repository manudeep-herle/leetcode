/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    const clean = new Set(nums);
    const sorted = [...clean].sort((a,b) => (b - a));
    return sorted[2] !== undefined ? sorted[2] : sorted[0]

};