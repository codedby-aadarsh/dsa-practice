class Solution {
    public boolean halvesAreAlike(String s) {
        String p=s.toLowerCase();
        int n=p.length();
       
        return vowel(p.substring(0,n/2))==vowel(p.substring(n/2,n));

    }
    static int vowel(String q){
        int count=0;
        for(int i=0;i<q.length();i++){
            if(q.charAt(i)=='a'||q.charAt(i)=='e'||q.charAt(i)=='i'||q.charAt(i)=='o'||q.charAt(i)=='u'){
                count++;
            }
        }
        return count;
    }
}