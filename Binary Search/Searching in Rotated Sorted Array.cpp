//🟩🟩🟩🟩RATNA ALWAYS prefer to COMPARE WITH RIGHT PERSON 💞💞❣️right person< or right person<= both gives correct answer
def bs(self,nums,target,left, right):
        while(left<=right):
            mid= (left+right)//2
            if(nums[mid] == target):return mid
            elif(nums[mid]>target):right=mid-1
            else: left=mid+1
        return -1

def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        temp=-1
        while(left<=right):
            mid= (left+right)//2
            if((mid ==0 or nums[mid]<nums[mid-1]) and (mid == len(nums)-1 or nums[mid+1]>=nums[mid])):
                temp=mid 
                break
            elif(nums[mid]>nums[len(nums)-1]):left=mid+1
            else : right= mid-1

        t1=self.bs(nums,target,0,mid-1)
        t2= self.bs(nums,target,mid,len(nums)-1)
        if(t1==-1 and t2==-1):return -1
        if(t1==-1):return t2
        return t1
