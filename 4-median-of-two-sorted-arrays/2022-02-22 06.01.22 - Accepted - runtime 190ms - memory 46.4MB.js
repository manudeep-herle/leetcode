/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    //Find the merge of the two
    const merge = []
    while(nums1.length || nums2.length){
        if(nums2.length === 0 || nums1[0] < nums2[0]){
            merge.push(nums1[0])
            nums1.shift()
        }else{
            merge.push(nums2[0])
            nums2.shift()
        }
    }
    const half = Math.floor(merge.length/2)
    if(merge.length %2)
        return merge[half]
    return (merge[half -1] + merge[half])/2

};