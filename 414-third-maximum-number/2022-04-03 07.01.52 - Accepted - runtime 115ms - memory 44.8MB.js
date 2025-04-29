/**
 * @param {number[]} nums
 * @return {number}
 */
var thirdMax = function(nums) {
    const clean = new Set(nums);
    console.log([...clean])
    const sorted = [...clean].sort((a,b) => (b - a));
    console.log("sorted", sorted)
    return sorted[2] !== undefined ? sorted[2] : sorted[0]

};