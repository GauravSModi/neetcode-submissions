class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) {
            return s.length();
        }

        int l = 0, r = 0;
        int res = 0;
        HashMap<Character, Integer> map = new HashMap();

        while (r < s.length()) {
            // if (l == r) {
            //     r ++;
            //     continue;
            // }

            // Seen this letter (and it's before l), not unique. Reset the string so that l is now at oldR + 1
            if (map.containsKey(s.charAt(r)) && map.get(s.charAt(r)) >= l) {
                l = map.get(s.charAt(r)) + 1;
            }

            // Haven't seen this letter before (or maybe we have),
            // so add it to (or overwrite the value in) the map
            map.put(s.charAt(r), r);

            res = Math.max(res, r-l+1);
            r++;
        }

        // int l = 0, r = 1;
        // int longestSubstringLength = 1;

        // HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        // map.put(s.charAt(l), l);

        // while (r < s.length()) {
        //     if (map.containsKey(s.charAt(r)) && map.get(s.charAt(r)) < l){
        //         // If the character was seen before l
        //         // if (map.get(s.charAt(r)) < l) {
        //             map.replace(s.charAt(r), r);
        //         // }
        //         // If it was after
        //         // else {
        //         //     l++;
        //         // }
        //     } else {
        //         if (map.containsKey(s.charAt(r)) && map.get(s.charAt(r)) > l){
        //             l = map.get(s.charAt(r)) + 1;
        //         } else {
        //             map.put(s.charAt(r), r);
        //             longestSubstringLength = Math.max(longestSubstringLength, r-l+1);
        //             System.out.println(l + " : " + r);
        //             r++;
        //         }
        //     }
        // }

        return res;
    }
}
