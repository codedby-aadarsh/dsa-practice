class Solution {
    public String reversePrefix(String word, char ch) {
        int index = word.indexOf(ch); // Find the first occurrence of 'ch'
        if (index == -1) {
            return word; // If 'ch' is not found, return the original word
        }
        
        // Reverse the prefix (substring up to index + 1)
        StringBuilder prefix = new StringBuilder(word.substring(0, index + 1)).reverse();
        // Return the reversed prefix concatenated with the rest of the string
        return prefix.append(word.substring(index + 1)).toString();
    }
}
