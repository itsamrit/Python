class Solution:
    def dfs (self, nums,i,temp,ans):
        if(i>=len(nums)):
            ans.append(temp.copy())     # Shallow copy if u are appending temp instead of temp, u are appending reference of temp, so when temp become empty and becomes list of empty list
            return

        temp.append(nums[i])            # ALWAYS APPEND FIRST 
        self.dfs(nums,i+1,temp,ans)
        temp.pop()
        while(i<len(nums)-1  and nums[i] == nums[i+1]): i+=1   #AFTER WHILE call dfs without appended elemet
        self.dfs(nums,i+1,temp,ans)
        

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        temp=[]
        nums.sort()
        self.dfs(nums,0,temp,ans)
        return ans
