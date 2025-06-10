class Solution {
    public int largestAltitude(int[] gain) {
     int[] list= new int[gain.length+1];
     int alt=0,max=0;
   for(int i=0;i<gain.length;i++){
        alt+=gain[i];
        list[i+1]=alt;
        if(list[i+1]>max){
            max=list[i+1];
        }
    }
    return max;
        
    }
}