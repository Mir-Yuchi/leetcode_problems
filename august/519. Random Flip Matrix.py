class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.d = {}

    def flip(self) -> List[int]:
        while True:
            r = random.randint(0, self.m*self.n-1)
            if r not in self.d:
                self.d[r] = 1
                return [r//self.n, r%self.n]

    def reset(self) -> None:
        self.d = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()