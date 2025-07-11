'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.'''



class Solution:
    def reverseVowels(self, s: str) -> str:
        s1=list(s)
        i=0
        j=len(s)-1
        v="aeiouAEIOU" 
        while(i<j):
            if(s1[i] in v and s1[j] in v):
                s1[i],s1[j]=s1[j],s1[i]
                i+=1
                j-=1
            if(s1[i] not in v):
                i+=1
            if(s1[j] not in v):
                j-=1
        return "".join(s1)
