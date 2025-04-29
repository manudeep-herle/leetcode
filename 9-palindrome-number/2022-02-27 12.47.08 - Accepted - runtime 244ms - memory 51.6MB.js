/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    x = x+"";
    x.split("")
    let i =0;
    let len = x.length;
    while(x[i] === x[len - 1 -i]){
if(len - 1- i === i || len - 1-(2 * i) === 1 )
    return true;
        i++;
    }
    return false
};