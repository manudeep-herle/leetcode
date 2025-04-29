/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let count = 0;
    let i = 0;
    while(i<flowerbed.length){
        if(flowerbed[i] === 0 && !flowerbed[i+1] && !flowerbed[i-1]){
            count ++;
            flowerbed[i] = 1;
        }
        i++;
    }
    console.log("count", count)
    return count >= n;
    //get rid of alternative number starting from the pos next to the first 1.
    
    
};

// 0,0,1,,0,,1,,0,,0,,0,,1,,1