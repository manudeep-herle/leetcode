/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
function repeated(s){
    const pure = [];
    for(i = 0; i< s.length; i++){
        if(!pure.includes(s.charAt(i))) pure.push(s.charAt(i))
        else return true;
    }return false;
}

var buddyStrings = function(s, goal) {
    if(goal.length !== s.length) return false;
    if(goal === s && repeated(s)) {
        console.log(repeated(s))
        return true
    };
 
    let anamolies = [];
    let source = s.split("");
    let target = goal.split("");
    for(i = 0; i< source.length; i++){
        if(source[i] !== target[i]){
            anamolies.push(i);
        }
    }
    console.log(anamolies)
    if(anamolies.length === 2 
       && source[anamolies[0]] === target[anamolies[1]] 
       && source[anamolies[1]] === target[anamolies[0]]) return true;
    
   return false;
    
    
};

