class Solution {
    public int countNegatives(int[][] grid) {
        int count=0;
        for(int[] ints:grid){
            for(int target:ints){
                if(target<0){
                    count++;
                }
            }
        }
        return count;
    }
}