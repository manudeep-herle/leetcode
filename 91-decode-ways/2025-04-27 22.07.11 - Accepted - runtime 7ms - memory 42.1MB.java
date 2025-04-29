class Solution {
    public int numDecodings(String s) {
        //  convert s to a array
        char[] chars = s.toCharArray();
        int[] mem = new int[s.length() + 1];
        mem[mem.length - 1] = 1;
        String lastCharStr = String.valueOf(chars[chars.length - 1]);
        int lastDigit = Integer.parseInt(lastCharStr);
        mem[mem.length - 2] = lastDigit > 0 ? 1 : 0;
        for (int i = s.length() - 2; i >= 0; i--) {
            if (chars[i] == '0') {
                mem[i] = 0; // no decoding starting with '0'
            } else {
                int twoDigit = Integer.parseInt("" + chars[i] + chars[i + 1]);
                if (twoDigit <= 26) {
                    mem[i] = mem[i + 1] + mem[i + 2];
                } else {
                    mem[i] = mem[i + 1];
                }
            }
        }
        return mem[0];
    }
}
