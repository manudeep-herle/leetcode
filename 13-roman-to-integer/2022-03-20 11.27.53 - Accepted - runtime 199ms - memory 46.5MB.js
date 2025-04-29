

const map = {
    "I": 1,
    "V":5,
    "X": 10,
    "L":50,
    "C": 100,
    "D": 500,
    "M":1000
}


/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    const hierarchy = Object.keys(map);
    let total = 0;
    for(i = 0; i< s.length; i++){
        let char = s.charAt(i)
        if(hierarchy.indexOf(char) < hierarchy.indexOf(s.charAt(i+1)))
        total -= map[char];
        else total += map[char];
    }
    return total;
};

//MCMXCIV
//1000 -100 + 1000 - 10 

