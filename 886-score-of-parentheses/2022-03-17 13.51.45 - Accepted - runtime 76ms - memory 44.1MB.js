/**
 * @param {string} s
 * @return {number}
 */
var scoreOfParentheses = function(S) {
    let len = S.length; 
        let pwr = 0;
        let ans = 0;
    for (let i = 0; i < len; i++)
 {       
        console.log(pwr)
        if (S.charAt(i) === "(") pwr++
        else if (S.charAt(i-1) === "(") ans += 2 ** --pwr
        else pwr--  
 }
    return ans
};