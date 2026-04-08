class Solution {
    public boolean hasDuplicate(int[] nums) {
        //use a map to check for dupes
        //loop through
        //if map contains num return true

        Set<Integer> numSet = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (numSet.contains(nums[i])) {
                return true;
            }
            numSet.add(nums[i]);
        }
        return false;
    }
}