function isSorted(arr){
    return arr.every((n, i) => n>arr[i-1])
}

var canBeIncreasing = function(arr) {
    var count = 0;
    const n = arr.length;
  
    var index = -1;
  
    for(i = 1; i < n; i++) 
    {
          
        // If arr[i-1] is greater than
        // or equal to arr[i]
        if (arr[i - 1] >= arr[i])
        {
              
            // Increment the count by 1
            count++;
  
            // Update index
            index = i;
        }
    }
  
    // If count is greater than one
    if (count > 1)
        return false;
  
    // If no element is removed
    if (count == 0)
        return true;
  
    // If only the last or the
    // first element is removed
    if (index == n - 1 || index == 1)
        return true;
  
    // If a[index] is removed
    if (arr[index - 1] < arr[index + 1])
        return true;
  
    // If a[index - 1] is removed
    if (arr[index - 2] < arr[index])
        return true;
  
    return false;
};