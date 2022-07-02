class Solution {
    public int removeElement(int[] nums, int val) {
     
        if(nums.length == 0){
            return 0;
        }
        
        int i = 0;
        int len = nums.length;
        while(i < len){
            if(nums[i] == val){
                nums[i] = nums[len - 1];
                len--;
            }
            else{
                i++;
            }
        }
        return len;
    }
}