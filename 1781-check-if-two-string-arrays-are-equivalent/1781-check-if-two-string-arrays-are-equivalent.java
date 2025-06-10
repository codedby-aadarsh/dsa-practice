class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
     int i=0;
     String s1="";
     String s2="";
     while(i<word1.length){
        s1+=word1[i];
        i++;
     }i=0;
      while(i<word2.length){
        s2+=word2[i];
        i++;
     }
     if(s1.equals(s2)){
        return true;
     }
      return false;
    
     } 
    }
