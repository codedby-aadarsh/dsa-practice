class Solution {
    public int findPeakElement(int[] nums) {
        if(nums.length==1){
            return 0;
        }
        else if(nums[0]>nums[1])
            return 0;
        else if(nums[nums.length-1]>nums[nums.length-2])
            return nums.length-1;
        else{
        for(int i=1;i<=(nums.length-1);i++){
            if(nums[i]>nums[i-1]&&nums[i]>nums[i+1]){
                return i;
            }
        }
        }
        return -1;
    }
}