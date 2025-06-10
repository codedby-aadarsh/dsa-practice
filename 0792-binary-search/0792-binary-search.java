class Solution {
    public int search(int[] nums, int target) {
        int start=0,left=nums.length-1;
        while(start<=left){
            int mid=start+(left-start)/2;
            if(target==nums[mid]){
                return mid;
            }else if(target>nums[mid]){
                start=mid+1;
            }else{
                left=mid-1;
            }
        }
        return -1;
    }
}