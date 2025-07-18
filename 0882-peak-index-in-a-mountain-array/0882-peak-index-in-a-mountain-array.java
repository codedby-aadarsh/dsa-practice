class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start=0,end=arr.length-1;
        while(start<=end){
            int mid=start+(end-start)/2;
            if(arr[mid]>arr[mid-1]){
                if(arr[mid]>arr[mid+1]){
                    return mid;
                }else{
                    start=mid;
                }
            }else{
                end=mid;
            }
        }
    return end;
    }
}