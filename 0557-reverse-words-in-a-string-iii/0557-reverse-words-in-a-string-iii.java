class Solution {
    public String reverseWords(String s) {
     String[] q= s.split(" ");
     String[] ans= new String[q.length];
     for(int i=0;i<q.length;i++){
       ans[i]=revrse(q[i]);
     }
     StringBuilder res= new StringBuilder();
     for(int i=0;i<ans.length;i++){
        if(i==ans.length-1)
            res.append(ans[i]);
        else
        res.append(ans[i]+" ");
     }
     return res.toString();

    }
    static String revrse(String n){
      String m="";
      for(int i=0;i<n.length();i++){
        m=n.charAt(i)+m;
      }
      return m;
           
        }
    }
