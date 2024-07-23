//😍😍Letter combination algo in 1 LINE : LAYER OF for loop in COMBINATION 01 algorithm : so we're passing c+1 unaffected by for loop's int i
//🟩🟩🟩🟩RATNA   ❤️❤️Since we're just adding a layer of loop in combination 01 algo to generate the strings, so our passing of 😍😍❤️❤️c is unaffected by loop's int i

class Solution:
    
    def dfs(self, digits, c, temp, ans, letterlist):    
        if(c == len(digits)):
            ans.append(temp)    # IN STRING IE TEMP there is no  temp.copy() . confirm once??
            return
        
        for i in letterlist[int(digits[c]) - 2]:
            temp += i
            self.dfs(digits, c + 1, temp, ans, letterlist)
            temp=temp[:len(temp)-1] # Remove last character

    def letterCombinations(self, digits: str) -> List[str]:
        letterlist = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        if(digits == "") :
            return ans
        self.dfs(digits, 0, "", ans, letterlist)
        return ans
