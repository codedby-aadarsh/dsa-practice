class Solution {
    public int diagonalSum(int[][] mat) {
        int count=0,n=mat.length-1;
        for(int i=0;i<mat.length;i++){
            count+=mat[i][i];
            count+=mat[i][n-i];
        }
        if(mat.length%2!=0){
            return count-mat[n/2][n/2];

        }
        return count;

    }
}