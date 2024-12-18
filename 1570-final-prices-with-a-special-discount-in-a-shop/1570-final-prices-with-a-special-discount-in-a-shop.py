class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st=[]
        for j in range(len(prices)):
            while st and prices[st[-1]]>=prices[j]:
                prices[st.pop()]-=prices[j]
            st.append(j)
        return prices