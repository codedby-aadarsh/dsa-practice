class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int[][] ans= new int[r][c];
        int row=0,col=0;
        if(r*c!=mat.length*mat[0].length){
            return mat;
        }
        for(int i=0;i<mat.length;i++){

            for(int j=0;j<mat[0].length;j++){
                ans[row][col]=mat[i][j];
                col++;
                if(col==c){
                    col=0;
                   
                    row++;
                }
                
            }
            
        }
        return ans;
        
    }
}