int maxSum(int arr[], int n, int k){
    int res = 0;
    for (int i=0; i<k; i++)res += arr[i];
    int curr_sum = res;    
    for (int i=k; i<n; i++){
       curr_sum += arr[i] - arr[i-k];
       res = max(res, curr_sum);
    } 
    return res;
}


Find all Anagram of p in a string s 

class Solution:
    from collections import defaultdict
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pp = defaultdict(int)
        ss = defaultdict(int)
        ans =[]
        if(len(p)> len(s)): return ans
        for i in range (0,len(p)):
            pp[p[i]]+=1
            ss[s[i]]+=1

        if(pp == ss): ans.append(0)
        for i in range(len(p),len(s)):
            ss[s[i-len(p)]]-=1
            if(ss[s[i-len(p)]] == 0) : del ss[s[i-len(p)]]
            ss[s[i]]+=1
            if(ss== pp): ans.append(i-len(p)+1)
        
        return ans


https://leetcode.com/problems/sliding-window-maximum/
// Sliding Window Maximum : Return a vector containing max of each window of size k
// tc=0(2*n)=o(n)  because deque takes o(1) in pop and push of first and last element unlike vector/array which take o(n) in pushing & pop first element
// 🟩Maintaining a monotonically decreasing deque having 1st element as largest


vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
	vector<int> res;
        deque<int>d;              // Here deque store index not value
    
        for(int i=0;i<k;i++){
            while(d.size() && nums[d.back()] < nums[i]) d.pop_back();   // pop if back is lesser than new element i,e nums[i]
            d.push_back(i);
        }
        res.push_back(nums[d.front()]);   // d.front () always have maximum value of that window & we will maintain this in next loop
        
        for (int i=k; i<n; i++) {
            if (d.size() && d.front() <= i-k) d.pop_front();      //pop if it is previous window's 1st element i,e it cant be part of current window
            while (d.size() && nums[d.back()] < nums[i]) d.pop_back();   // pop if back is lesser than new element i,e nums[i]
            d.push_back(i);  
            res.push_back(nums[d.front()]);
        }
        
        return res;
}
