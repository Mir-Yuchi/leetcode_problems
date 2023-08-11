class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        strs.sort(key=len, reverse=True)
        for i, word in enumerate(strs):
            if all(not isSubsequence(word, strs[j]) for j in range(len(strs)) if i != j):
                return len(word)
        return -1