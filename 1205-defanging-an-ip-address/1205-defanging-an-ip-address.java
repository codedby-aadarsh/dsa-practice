class Solution {
    public String defangIPaddr(String ad) {
       // char c='[.]';
        String ans="";
        for(int i=0;i<ad.length();i++){
            if(ad.charAt(i)=='.'){
                ans+="[.]";
            }else{
                ans+=ad.charAt(i);
            }
        }
        return ans;
    }
}