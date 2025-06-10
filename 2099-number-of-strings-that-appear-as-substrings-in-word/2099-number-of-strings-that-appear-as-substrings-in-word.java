class Solution {
    public int numOfStrings(String[] ps, String word) {
        int count=0;
        for(int i=0;i<ps.length;i++){
            if(word.contains(ps[i])){
                count++;
            }
        }
        return count;
    }
}