/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let arrNo = 0;
    let arr = [];
    let increment = true;
    for(i =0; i< s.length; i++){
        if(!arr[arrNo]) arr[arrNo] = [];
        arr[arrNo].push(s.charAt(i));
        if(arrNo === numRows - 1)
            increment = false;
        else if(arrNo === 0)
            increment = true;
        if(increment) arrNo++; 
        else if(arrNo > 0) arrNo--;
    }
    // console.log(arr);
    // console.log(arr.flat().join(''))
    return arr.flat().join('')
};

