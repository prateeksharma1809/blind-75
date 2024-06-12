package com.leetcode.arrays;

import java.util.Arrays;
import java.util.Stack;

public class ValidParentheses {
	
	public boolean isValid(String s) {
		
		Stack<Character> stack = new Stack<>();
		for(int i=0; i<s.length();i++) {
			if(Arrays.asList('(','{','[').contains(s.charAt(i))) {
				stack.push(s.charAt(i));
			}else if (!stack.isEmpty() && ((s.charAt(i)=='}' && stack.peek()=='{') || (s.charAt(i)==']' && stack.peek()=='[') 
					|| (s.charAt(i)==')' && stack.peek()=='('))) {
				stack.pop();
			}else {
				return false;
			}
			
		}
        return stack.size()==0;
    }

	public static void main(String[] args) {
		ValidParentheses vp = new ValidParentheses();
		System.out.println(vp.isValid("[{]}"));
	}

}
