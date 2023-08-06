class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()

        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)

        diff = (bobSum - aliceSum) // 2

        for alice in aliceSizes:
            bob = alice + diff
            if bob in bobSizes:
                return [alice, bob]