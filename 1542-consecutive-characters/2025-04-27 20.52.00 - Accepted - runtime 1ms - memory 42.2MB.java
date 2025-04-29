import java.util.*;

class Solution {
    public int maxPower(String s) {
        // if s.length() == 1, return 1
        if (s.length() == 1) {
            return 1;
        }
        // loop through the string s, 
        char[] chars = s.toCharArray();
        // compare s[i] with s[i-1], 
        int res = 1;
        int curPower = 1;

        for (int i = 1; i < chars.length; i++) {
            // increment curPower if they are the same, 
            if (chars[i] == chars[i - 1]) {
                curPower++;
            } else {
                // res = max(res, curPower)
                res = Math.max(res, curPower);
                // set curPower = 1 if they are different. 
                curPower = 1;
            }
        }
        res = Math.max(res, curPower);
        // return res
        return res;
    }
}