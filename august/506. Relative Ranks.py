class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        if n == 1: return ['Gold Medal']
        if n == 2: return ['Gold Medal', 'Silver Medal'] if score[0] > score[1] else ['Silver Medal', 'Gold Medal']
        rank = sorted(score, reverse=True)
        ans = []
        for i in range(n):
            if score[i] == rank[0]: ans.append('Gold Medal')
            elif score[i] == rank[1]: ans.append('Silver Medal')
            elif score[i] == rank[2]: ans.append('Bronze Medal')
            else: ans.append(str(rank.index(score[i])+1))
        return ans