TC : o(n*logn) n for checking is all subarrays can be divided into k parts with max cap mx & logn for binary search of max cap mx.
// KOKO EATING BANANAS : array of n to be split in n+k size opposite of this

def valid(self,mid, h, piles):
        temph = 0
        for pile in piles:
            temph += (pile + mid - 1) // mid
        
        return temph <= h


def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = -1
        for i in range (0,len(piles)):
            right = max(right,piles[i])
        ans = right
        while(left<=right):
            mid = (left+right)//2
            if(self.valid(mid,h,piles)):  
                ans = mid
                right= mid-1
            else :
                left=mid+1
        
        return math.ceil(ans)      
