//😍😍Letter combination algo in 1 LINE : LAYER OF for loop in COMBINATION 01 algorithm : so we're passing c+1 unaffected by for loop's int i
//🟩🟩🟩🟩RATNA   ❤️❤️Since we're just adding a layer of loop in combination 01 algo to generate the strings, so our passing of 😍😍❤️❤️c is unaffected by loop's int i

class Solution:
    def dfs(self, arr, m, c, temp, ans):
        if len(temp)==len(arr):
            ans.append(temp)
            return

        for i in range(len(m[int(arr[c])])):
            self.dfs(arr, m, c+1, temp+m[int(arr[c])][i], ans)
            

    def letterCombinations(self, digits: str) -> List[str]:
        m=["","","abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans =[]
        if len(digits)==0:
            return ans
        self.dfs(digits, m, 0, "", ans)
        return ans
