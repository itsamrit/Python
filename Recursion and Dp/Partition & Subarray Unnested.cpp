//✅✅DEPENDENT ON ADJACENT SUBARRAY FORMED
//🟩🟩WORD BREAK : SPECIAL PROB :MEMO WITH MAP
//🟢If non indepenet of adjacent subarray, then u can run 2 loop to check iteratively check all subarray.o(n^2) but most of indepent questions are solved using sliding window or some technique descriped in SUBARRAY repo

Tc:n^2 

TYPE 1 DP : BASED ON CHECKING EACH SUBSTRING
// Word break  & Palindrome Partitioning

int f(int i,int n,string &str,vector<int>&dp){
    if(i==n) return 0;
    if(dp[i]!=-1)return dp[i];
    dp[i]=INT_MAX;            
    
    for(int j=i;j<n;j++){
        if(palindrome(i,j,str))  // For word break : if(s.find(s.substr(i, j-i+1))!= s.end()){.. 
           dp[i]=min(dp[i] , 1 + f(j+1,n,str,dp));
     }
     return dp[i];
}

int solve(string str){
    int n=str.size();    // For word break store all words dictionary in a set<int>s 
    vector<int>dp(n,-1);
    return f(0,n,str,dp) -1;
}
