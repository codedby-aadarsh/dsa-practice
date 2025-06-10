class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0, right = nums.length - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;

            // Ensure mid is always even
            if (mid % 2 == 1) {
                mid--;
            }

            // Check if the pair is valid or invalid
            if (nums[mid] == nums[mid + 1]) {
                // The single element is in the right half
                left = mid + 2;
            } else {
                // The single element is in the left half or mid is the single element
                right = mid;
            }
        }

        return nums[left];
    }
}
