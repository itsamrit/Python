# 🟩🟩U need to cross match all words of dictionary to all words formed from string 
# // More similar problems to word break : Extra Characters in a String
# // Method 2 : You just need to match all words with all dictionary.  So instead of searching each string in dictionary , you can do vice versa.
# //     🟩In dp there is no optimization that u start from smallest or largest word. Start from anywhere, u need to cross match all words of dictionary to all words formed from string and find min or max or whatever is asked.
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        st = set(wordDict)
        dp = [-1] * (len(s) + 1)

        def dfs(c):
            if c >= len(s):
                return 0
            if dp[c] != -1:
                return dp[c]
            
            mini = 10**9
            
            for i in range(c, len(s)):
                if s[c:i+1] in st:
                    mini = min(mini, dfs(i + 1))
            
            dp[c] = min(mini, 1 + dfs(c + 1))
            return dp[c]

        return dfs(0) == 0
