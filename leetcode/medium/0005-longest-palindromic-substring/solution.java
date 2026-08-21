class Solution {
    private int expandFromCenter(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            left--;
            right++;
        }
        return right - left - 1;
    }

    public String longestPalindrome(String s) {
        int bestStart = 0;
        int bestLength = 1;
        for (int i = 0; i < s.length(); i++) {
            int oddLength = expandFromCenter(s, i, i);
            int evenLength = expandFromCenter(s, i, i + 1);
            int longer = Math.max(oddLength, evenLength);
            if (longer > bestLength) {
                bestLength = longer;
                bestStart = i - (longer - 1) / 2;
            }
        }
        return s.substring(bestStart, bestStart + bestLength);
    }
}