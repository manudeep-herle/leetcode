/**
 * @param {string} s
 * @return {boolean}
 */
const map = {
    ")": "(",
    "]": "[",
    "}": "{"
}

var isValid = function(s) {
    let arr = s.split("");
    let stack = [];
    arr.forEach((brack, i) => {
        if(map[brack] && stack[stack.length - 1] === map[brack]){
            stack.pop();
        }
        else stack.push(brack)
    })
    console.log(stack)
    if(stack.length !== 0) return false
    return true;
};