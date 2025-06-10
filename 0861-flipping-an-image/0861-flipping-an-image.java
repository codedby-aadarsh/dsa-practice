class Solution {
     public int invert(int value){
                if(value==1){
                    return 0;
                }
                else{
                    return 1;}
            }
    public int[][] flipAndInvertImage(int[][] image) {
        int start=0,end=image.length-1,temp=0;
        for(int i=0;i<image.length;i++){
            start=0;
            end=image.length-1;
            for(int j=0;j<image[i].length&&start<=end;j++){
                temp = invert(image[i][start]);
                image[i][start]=invert(image[i][end]);
                image[i][end]=temp;
                start++;
                end--;
            }
            
           
        }
        return image;
    }
}