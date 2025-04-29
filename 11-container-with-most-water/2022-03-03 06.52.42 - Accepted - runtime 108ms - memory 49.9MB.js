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
            let w = j - i;
            if(h*w > max) max = h*w;
        h === height[i] ? i++: j--;
    }
    return max;
};


    // let max = 0;
    // for(i =0; i<height.length - 1; i++){
    //     for(j=i+1; j<height.length; j++){
    //         let h = Math.min(height[i], height[j])
    //         let w = j - i;
    //         if(h*w > max) max = h*w;
    //     }
    // }
    // return max;