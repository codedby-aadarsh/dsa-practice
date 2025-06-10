class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = 0;
        ArrayList<Boolean> child = new ArrayList<>(candies.length);
        for (int a : candies) {
            if (a > max) {
                max = a;
            }
        }
        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= max) {
                child.add(true);

            } else {
                child.add(false);
            }

        }
        return child;
    }
}