import java.util.*;

class Solution {
    public boolean checkIfPangram(String sentence) {
        char[] chars = sentence.toCharArray();
        HashSet<Character> charSet = new HashSet<>();
        for (char c : chars) {
            charSet.add(c);
        }
        if (charSet.size() == 26) {
            return true;
        }
        return false;
    }
}