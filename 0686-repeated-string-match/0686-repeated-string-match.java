class Solution {
    public int repeatedStringMatch(String a, String b) {
     String p="";
     int count=0;
     int n=b.length()/a.length();
     for(int i=0;i<n;i++){
       p+=a;
       if(b.equals(p)){
        return i+1;
     } 
     }
        p=p+a;
        if(p.contains(b)){
            return n+1;
        }
         p=p+a;
        if(p.contains(b)){
            return n+2;
        }

        
    
     return -1; 
    }
}