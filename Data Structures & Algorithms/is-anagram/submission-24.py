class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        _s=sorted(s)
        _t=sorted(t)
        return _s==_t