class Solution {
    public int mySqrt(int x) {
        int l = 0;
        int r = x;
        int last = 0;
        while (l <= r){
            int mid = (l+r)/2;
            long prod = (long) mid * mid;
            if(prod == x){
                return mid;
            }else if(prod < x){
                last = mid;
                l = mid + 1;                
            } else {
                r = mid - 1;
            }
        }
        return last;
    }
}