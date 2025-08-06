class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans=0
        dici={}
        for i in stones:
            if i in dici:
                dici[i]+=1
            else:
                dici[i]=1
        for i in range(len(jewels)):
            ch=jewels[i]
            if ch in dici:
                ans+=dici[ch]
        return ans 