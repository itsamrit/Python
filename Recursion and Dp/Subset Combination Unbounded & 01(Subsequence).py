class Solution:
    def dfs (self, nums,i,temp,ans):
        if(i>=len(nums)):
            ans.append(temp.copy())
            return

        temp.append(nums[i])
        self.dfs(nums,i+1,temp,ans)
        temp.pop()
        while(i<len(nums)-1  and nums[i] == nums[i+1]): i+=1
        self.dfs(nums,i+1,temp,ans)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()
        self.dfs(nums,0,temp,ans)
        return ans
