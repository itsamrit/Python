def dfs (self, nums , c, temp, ans):
    if c>=len(nums):
        ans.add(tuple(temp)) # or ans.add(list(temp)) 
        return 
    self.dfs(nums, c+1, temp, ans)
    temp.append(nums[c])
    self.dfs(nums, c+1, temp, ans)
    temp.pop()
    

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    ans =set()
    nums = sorted(nums)  # let arr=[1,2,1] then if not sorted [1,2] and [2,1] but they are same combination, TO avoid this we use the sorted with combination of set() 
    self.dfs(nums, 0, [], ans)
    return list(ans)
