class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        if len(s)%k==0:
            return '-'.join([s[i:i+k] for i in range(0,len(s),k)])
        else:
            return '-'.join([s[:len(s)%k]]+[s[i:i+k] for i in range(len(s)%k,len(s),k)])