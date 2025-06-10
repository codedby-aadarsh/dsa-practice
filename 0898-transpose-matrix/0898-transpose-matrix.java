class Solution {
    public int[][] transpose(int[][] matrix) {
        int n= matrix.length-1,temp=0;
        int[][] list = new int[matrix[0].length][n+1];
        
        for(int i=0;i<n+1;i++){
            for(int j=0;j<matrix[0].length;j++){
                list[j][i]=matrix[i][j];
            }
        }

        return list;
        }
       
    
}