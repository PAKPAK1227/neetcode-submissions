class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean flag = false;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j] && j!= i) {
                    return true;
                }
            }
        }
        return false;

    }
}