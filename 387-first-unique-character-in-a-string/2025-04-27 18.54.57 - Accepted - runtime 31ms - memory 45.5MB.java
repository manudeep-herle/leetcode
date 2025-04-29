import java.util.HashMap;

class Solution {
    public int firstUniqChar(String s) {
        HashMap<Character, Integer> counts = new HashMap<Character, Integer>();
        // find the freq of each char in s
        for (int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            Integer count = counts.getOrDefault(c, 0) + 1;
            counts.put(c, count);
        }
        // iterate through s and return the first char with freq = 1
        for (int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if(counts.get(c) == 1){
                return i; 
            }
        }
        return -1;
    }
}