class Solution:
    def distMoney(self, money: int, children: int) -> int:
        ans=(money-children)//7
        if children>money:
            return -1

        elif ans==children-1 and (money-children)%7==3:
            return ans-1
        
        elif ans==children and (money-children)%7>0:
            return ans-1

        elif children<ans:
            return children-1

        return ans