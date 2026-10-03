class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> openBrackets = new HashMap<Character, Character>();
        openBrackets.put(')', '(');
        openBrackets.put('}', '{');
        openBrackets.put(']', '[');

        for (int i = 0; i < s.length(); i ++) {
            // If it's an opening bracket
            if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {
                stack.push(s.charAt(i));
            // If it's a closing bracket 
            } else {
                // 
                if (!stack.isEmpty()){
                    char currBracket = stack.pop();
                    if (currBracket != openBrackets.get(s.charAt(i))){
                        return false;
                    }
                } else {
                    return false;
                }
            }
        }

        return (stack.isEmpty()) ? true : false;
    }
}
