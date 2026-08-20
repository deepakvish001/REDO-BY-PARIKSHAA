class Solution {
    public int[] resultArray(int[] nums) {
        List<Integer> li1=new ArrayList<>();
        List<Integer> li2=new ArrayList<>();
        li1.add(nums[0]);
        li2.add(nums[1]);
        int i=0;
        int j=0;
        for(int n=2;n<nums.length;n++){
            if(li1.get(i)>li2.get(j)){
                li1.add(nums[n]);
                i++;
            }
            else{
                li2.add(nums[n]);
                j++;
            }
        }
        int[] arr=new int[nums.length];
        int p=0;
        for(int h=0;h<li1.size();h++){
            arr[p]=li1.get(h);
            p++;
        }
        for(int h=0;h<li2.size();h++){
            arr[p]=li2.get(h);
            p++;
        }
        return arr;
    }
}