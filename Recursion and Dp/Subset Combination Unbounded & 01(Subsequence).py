def dfs (self, nums , c, temp, ans):
    if c>=len(nums):
        ans.add(tuple(temp))
        return 
    self.dfs(nums, c+1, temp, ans)
    temp.append(nums[c])
    self.dfs(nums, c+1, temp, ans)
    temp.pop()
    

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    ans =set()
    nums = sorted(nums)
    self.dfs(nums, 0, [], ans)
    return list(ans)
