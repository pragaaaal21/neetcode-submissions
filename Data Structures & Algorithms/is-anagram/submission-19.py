class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x={}
        y={}

        for ch in s:
            x[ch]=x.get(ch,0)+1
        for ch in t:
            y[ch]=y.get(ch,0)+1
        return x ==y