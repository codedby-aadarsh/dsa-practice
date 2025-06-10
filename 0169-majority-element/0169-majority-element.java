class Solution {
    public int majorityElement(int[] nums) {
        int count=0,candidate=0;
        for(int a:nums){
            if(count==0){
                candidate=a;
                
            } if(candidate==a){
                count++;
            }else{
                count--;
            }
            
        }
 return candidate;     
}  
}