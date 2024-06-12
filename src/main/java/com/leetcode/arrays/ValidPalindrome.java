package com.leetcode.arrays;

public class ValidPalindrome {
	public boolean isPalindrome(String s) {
		s= s.toLowerCase().replaceAll("[^a-zA-Z0-9]", "");
		System.out.println(s);
		int i=0, j =s.length()-1;
		while(i<j && s.charAt(i)==s.charAt(j)) {
			i++;
			j--;
		}
		if(i>=j) {
			return true;
		}
		return false;
	}

	public static void main(String[] args) {
		ValidPalindrome vp = new ValidPalindrome();
		System.out.println(vp.isPalindrome("A man, a plan, a canal: Panama"));
	}

}
