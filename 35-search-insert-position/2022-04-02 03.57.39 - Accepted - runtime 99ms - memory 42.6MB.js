/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    
    const index  = nums.findIndex((num, i) => {
        if(num >= target) {
            console.log(num, i, num >= target)
            return true;
        };
    })
    console.log(index);
    return index >= 0 ? index : nums.length;
};