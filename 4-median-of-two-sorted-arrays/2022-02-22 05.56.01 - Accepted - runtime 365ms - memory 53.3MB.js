/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    //Find the merge of the two

    let merge = []
    while(nums1.length || nums2.length){
        if(nums2.length === 0 || nums1[0] < nums2[0]){
            merge.push(nums1[0])
            nums1.splice(0,1)
        }else{
            merge.push(nums2[0])
            nums2.splice(0,1)
        }
    }
    console.log(merge);
    let length = merge.length;
    let median = 0;
    if(length % 2 === 0){
        median = (merge[length/2] + merge[length/2 - 1])/2
    }else{
        median = merge[Math.floor(length/2)]
    }
    
    return median;
};