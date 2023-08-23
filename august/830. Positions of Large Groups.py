class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        cur = 0
        for i in range(len(s)):
            if s[i]!=s[cur]:
                if i-cur>=3:
                    ans.append([cur,i-1])
                cur = i
        if len(s)-cur>=3:
            ans.append([cur,len(s)-1])
        return ans