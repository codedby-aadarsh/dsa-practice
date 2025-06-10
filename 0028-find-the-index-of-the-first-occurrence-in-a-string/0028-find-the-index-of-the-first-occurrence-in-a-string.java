class Solution {
    public int strStr(String haystack, String needle) {
        return indx(haystack,needle,needle.length(),0);
    }
    static int indx(String p, String q,int n,int ind){
        if(p.length()<n){
            return -1;
        }
        return p.substring(0,n).equals(q)?ind:indx(p.substring(1),q,n,ind+1);
    }
}