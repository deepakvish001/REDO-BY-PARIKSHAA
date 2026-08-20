class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int n = nums1.length;
        int m = nums2.length;
        int low = 0;
        int high = n;

        while (low <= high) {
            int x = low + (high - low) / 2;
            int y = (n + m + 1) / 2 - x;
            int l1 = (x == 0) ? Integer.MIN_VALUE : nums1[x - 1];
            int r1 = (x == n) ? Integer.MAX_VALUE : nums1[x];
            int l2 = (y == 0) ? Integer.MIN_VALUE : nums2[y - 1];
            int r2 = (y == m) ? Integer.MAX_VALUE : nums2[y];
            // Correct partition
            if (l1 <= r2 && l2 <= r1) {
                // Odd total length
                if ((n + m) % 2 == 1) {
                    return Math.max(l1, l2);
                }
                // Even total length
                return (Math.max(l1, l2) + Math.min(r1, r2)) / 2.0;
            }
            // Too many elements from nums1
            if (l1 > r2) {
                high = x - 1;
            } 
            // Too few elements from nums1
            else {
                low = x + 1;
            }
        }
        return 0;
    }
}