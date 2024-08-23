package com.oa;

import java.util.Arrays;

public class CountVowelSubString {
	private boolean isVowel(char c) {
		if(Arrays.asList('a','e','i','o','u').contains(c)) {
			return true;
		}
		return false;
	}
	// https://leetcode.com/problems/count-vowel-substrings-of-a-string/
	public int countVowelSubstrings(String word) {
		int result=0;
//		for(int i=0;i<word.length();i++) {
//			HashSet<Character> set = new HashSet<>();
//			for(int j=i;j<word.length() && isVowel(word.charAt(j));j++) {
//				set.add(word.charAt(j));
//				if(set.size()>=5) {
//					result++;
//				}
//			}
//		}
		return result;
	}

	public static void main(String[] args) {
		CountVowelSubString cs = new CountVowelSubString();
		System.out.println(cs.countVowelSubstrings("cuaieuouac"));

	}

}
