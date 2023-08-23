class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def isPrime(n):
            if n==1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        ans=0
        for i in range(left,right+1):
            if isPrime(bin(i).count('1')):
                ans+=1
        return ans