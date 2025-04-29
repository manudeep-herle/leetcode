/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
let max = 0;
    let i = 0;
    let j = height.length -1;
    while(j>i){
            let h = Math.min(height[i], height[j])
            if(h*(j - i) > max) max = h*(j - i);
        h === height[i] ? i++: j--;
    }
    return max;
};


