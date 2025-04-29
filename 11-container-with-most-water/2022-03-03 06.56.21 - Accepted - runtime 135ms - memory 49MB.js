/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
let max = 0;
    let i = 0;
    let j = height.length -1;
    while(j>i){
            let h 
            let w = j-i;
            if(height[i] < height[j]){
                h = height[i]
                i++
            }else {
                h = height[j]
                j--;
            }
        
            if(h*w > max) max = h*w;
    }
    return max;
};


