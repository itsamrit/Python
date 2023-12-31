// Like all other dp questions all permutation except printing can be solved using adding dp
//     eg: finding no of permutations having sum equal to target (1d dp since in void dfs(..,int sum) only 1 variable sum)

class Solution:
    def dfs (self, nums, temp, ans,vis):                              #😍😍😍we dont pass index c in permutation, we call dfs for i=0 to nums.size() 
        if(len(temp)==len(nums)):
            ans.append(temp.copy())
            return
        
        for c in range(0,len(nums)):
            if(vis[c]==0):                                             #Remove for unbounded
                if(c>0 and nums[c]== nums[c-1] and vis[c-1]): return   #Remove for unbounded
                vis[c]=1                                               #Remove for unbounded
                temp.append(nums[c])
                self.dfs(nums,temp,ans,vis)                             #😍We check vis[i] but we dont pass index c in permutation, we call dfs for i=0 to nums.size()
                vis[c]=0                                                #✅Unmark it so that element can be permuted with other things also//Remove for unbounded
                temp.pop()


    def permute(self, nums: List[int]) -> List[List[int]]:
        temp=[]
        ans=[]
        vis=[0]*len(nums)
        self.dfs(nums,temp,ans,vis)
        return ans


// Rule : For bounded: If elements of input array may have same elements eg: 112, u cant remove them like , u have to necessarily use if(i>c && cand[i]==cand[i-1])continue; i,e 112 will be formed only 1 time in combination
//         eg:If frequency of element given(how much times elements has occured) it comes under bounded & use if(i>c&&..) to avoid duplicates
// Rule : For unbounded: All elements must be necessarily be unique. No question till now of unbounded asked with similar elements but if asked remove duplicate elements before recursive code.
//         eg: Generate Parenethesis of size n. eg: ()))(( IF we use bounded then we need to sort like (((()))). 
//           Now we can either use unounded comb/perm code for ((())) for(2times ()) or write without for loop since there are only 2 elements  
//           Note: comb of ((())) : Since elements are not unique we necessarily have to use if(i>c&& ..) & hence only 1 combinatio will be formed ((()))
