class Solution {
    public boolean isPalindrome(String s) {
       String result =s.toLowerCase().replaceAll("[\\s\\p{Punct}]", "");
       
       for(int i=0;i<result.length()/2;i++){
        if(result.charAt(i)!=result.charAt(result.length()-i-1)) return false;
       }
       return true;
    }
}