/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    let result = "";
    for(i=0; i< strs[0].length; i++){//through the first string
        let char = strs[0].charAt(i)
        for(j=0; j< strs.length; j++){ // through the array of strings
            if(strs[j].charAt(i) !== char){
              return result  
            }
        }
        result += char;
    }
    return result;
    
};