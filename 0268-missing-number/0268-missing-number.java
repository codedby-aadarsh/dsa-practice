class Solution {
    public int missingNumber(int[] nums) {
      int n=nums.length;
      int sum1=n*(n+1)/2,sum2=0;
      for(int a: nums){
        sum2+=a;
      }
      return sum1-sum2;
    }
}