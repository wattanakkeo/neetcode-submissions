class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //Track the frequency of how many times the word has each 
        //letter in the alphabet
            //Turn that frequency into a key. If it's an anagram 
            //they have the same fequency
            //Store it into a hashmap with an ArrayList
        
        Map<String, ArrayList<String>> anagrams = new HashMap<>();
        
        for (String word : strs) {
            int[] frequency = new int[26];
            for (char letter : word.toCharArray()) {
                frequency[letter - 'a']++;
            }
            String key = Arrays.toString(frequency);
            anagrams.putIfAbsent(key, new ArrayList<>());
            anagrams.get(key).add(word);
        }
        return new ArrayList<>(anagrams.values());
    }
}
