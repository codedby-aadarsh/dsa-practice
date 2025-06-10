class Solution {
    public boolean judgeCircle(String moves) {
       int count=0;
       for(int i=0;i<moves.length();i++){
          count+=(cnt(moves.charAt(i)));
       } 
       return count==0;
    }
    static int cnt(char c){
        switch(c){
            case 'L': return -1;
            case 'R': return +1;
            case 'U': return +4;
            case 'D': return -4;
            default: return 0;
        }
    }
}