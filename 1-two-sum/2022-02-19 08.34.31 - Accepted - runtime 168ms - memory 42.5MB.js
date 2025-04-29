/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for( i =0; i < nums.length ; i++){
        const j = nums.indexOf(target - nums[i])
        if(j>-1 && j!== i) return [i,j] 
    }
};