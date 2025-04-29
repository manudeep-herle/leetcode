var lengthOfLongestSubstring = function(s) {
    //Loop through string
    const arr  = s.split("");
    const result = []
    for(i = 0; i<arr.length; i++){
        let temp = [];
        for(j=i; j<arr.length;  j++){
            if(!temp.includes(arr[j])) temp.push(arr[j])
            else break;
        }
        result.push(temp)
    }
    console.log(result)
    let ioflarge= 0;
    result.map((arr,i) => {
        if(arr.length > ioflarge) {
            ioflarge = arr.length
        }
    })
    return ioflarge;
    
    //Starting at each index find the largest string
    //Get the largest of these large strings.
};