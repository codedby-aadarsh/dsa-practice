class Solution {
    public int arrangeCoins(int n) {
        int count=0,i=1;
       while(n-i>=0){
        
            count++;
            
            n=n-i;
            i++;

       }
       return count;
    }
}