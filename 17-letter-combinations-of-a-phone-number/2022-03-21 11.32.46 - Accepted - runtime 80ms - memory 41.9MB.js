const map = {
    1:[],
    2:["a","b","c"],
    3:["d","e","f"],
    4:["g", "h", "i"],
    5:["j","k","l"],
    6:["m","n","o"],
    7:["p","q","r","s"],
    8:["t","u","v"],
    9:["w","x","y","z"],
}

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    const arr = (digits+"").split("");
    const len = arr.length;//2
    let result = [];
    console.log(arr[0], map[arr[0]]);
    if(len === 1){
        result = map[arr[0]]
    }
    else if(len === 2){
        for(i=0; i< map[arr[0]].length; i++){
            for(j=0; j< map[arr[1]].length; j++){
                result.push(map[arr[0]][i] + map[arr[1]][j]);
            }
        }
    } 
    else if(len === 3){
        for(i=0; i< map[arr[0]].length; i++){
            for(j=0; j< map[arr[1]].length; j++){
                for(k=0; k<map[arr[2]].length; k++){
                    result.push(map[arr[0]][i] + map[arr[1]][j] + map[arr[2]][k]);
                }
            }
        }
    }
    else if(len===4){
          for(i=0; i< map[arr[0]].length; i++){
            for(j=0; j< map[arr[1]].length; j++){
                for(k=0; k<map[arr[2]].length; k++){
                    for(l=0; l<map[arr[3]].length; l++)
                        result.push(map[arr[0]][i] + map[arr[1]][j] + map[arr[2]][k] + map[arr[3]][l] );
                }
            }
        }
    }
    return result;
};


