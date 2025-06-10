class Solution {
    public int numIdenticalPairs(int[] nums) {
        int pair=0,n=nums.length;
        for(int i= 0;i<n;i++){
            
            for(int j=0;j<n;j++){
            if(nums[i]==nums[j]&&i<j){
                pair++;
            }
            }
        }
        return pair;
    }
}