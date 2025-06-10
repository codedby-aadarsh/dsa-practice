class Solution {
    public int findKthPositive(int[] arr, int k) {
        int count=0,element=1,i=0;
        while(count<k){
           if(i<arr.length&&arr[i]==element){
            i++;
           }
           else{
            count++;
            if(count==k){
                return element;
            }
           }
           element++;
        }

     return -1;
    }
}