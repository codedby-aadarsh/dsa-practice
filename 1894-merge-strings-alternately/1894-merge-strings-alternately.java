class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder ans= new StringBuilder();
        int start=0,end=0;
        while(start<word1.length()||end<word2.length()){
            if(start<=word1.length()-1) ans.append(word1.charAt(start));
              if(end<=word2.length()-1)  ans.append(word2.charAt(end));
            start++;
            end++;

        }
    return ans.toString();
    }
}