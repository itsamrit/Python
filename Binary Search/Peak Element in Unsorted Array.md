![peak element in unsorted array](https://github.com/itsamrit/DSA/assets/86003701/5b8b6778-ba9c-4a6b-aeaa-aa7a26cbd96d)

```

def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end=len(nums)-1
        while(start<=end):
            mid = ceil((start+end)/2)
            if( mid-1<0 or nums[mid-1] < nums[mid]  ) and ( mid+1==len(nums) or nums[mid+1]<nums[mid] ) :
                return mid
            elif mid-1>=0 and nums[mid-1] > nums[mid] :
                end = mid-1
            else:
                start = mid+1
        
        return -1


