class Solution {
    public int lengthOfLastWord(String s) {
       s=s.trim();
        int n=s.length(),count=0;
        if(n==1) return 1;
       for(int i=n-1;i>=0;i--){
        if(s.charAt(i)!=' '){
            count++;
        }else{
            return count;
        }
       } 
       return count;
    }
}