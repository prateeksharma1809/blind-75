package com.leetcode.arrays;

import java.util.regex.Pattern;

public class ValidWord {
	public boolean isValid(String word) {
		if(word.length()<3) 
			return false;
		Pattern p = Pattern.compile("[^a-zA-Z0-9]");
		if(p.matcher(word).find())
			return false;
		
		boolean v = Pattern.compile("[aeiouAEIOU]").matcher(word).find();
		boolean c =  Pattern.compile("[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z]").matcher(word).find();
        if(c && v)
        	return true;
        return false;
    }

}
