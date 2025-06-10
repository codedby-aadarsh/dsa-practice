class Solution {
    public String interpret(String c) {
     StringBuilder ans =new StringBuilder();
     int i=0;

    while(i<c.length()){
        if(c.charAt(i)=='G'){
            ans.append('G');
            i++;
            continue;
        }else if(c.charAt(i)=='('){
            if(c.charAt(i+1)==')'){
                ans.append('o');
                i+=2;
                continue;
                }
            else if(c.charAt(i+1)=='a'){
                ans.append("al");
                i+=4;
                continue;}
        }else{
            ans.append(c.charAt(i));
            i++;
        }
     }
      return ans.toString();   
    }
}