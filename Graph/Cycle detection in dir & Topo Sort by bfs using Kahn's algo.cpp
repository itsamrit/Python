Direct Cyle BFS : Kahn algorithm : If topological sort not possible than there is cycle
// Indegree is no of edges coming towards or inside node & Outdegree is no of edges going out from node. In undirected both are same.
// One graph can have multiple toposort 
// Here we dont convert dfs into bfs instead we use kahn algo if topo order found no cycle else cycle
// 🟩Problem that can only be solved by kahn bfs algo & cant be solved by dfs topo : Minimum Height Trees
//         🟩Minimum Height Trees : give all root node starting from which graph has min height : store all leaf node having indeg =1 in queue & start when indeg[1]q.push instead of indeg[o] in for(auto i:g[c])

//We can find outdegree.But for toposort indegree is required, so reverse graph and find indegree (which will outdegree of original graph)
https://leetcode.com/problems/find-eventual-safe-states/description/  
🟩Problem that can only be solved by kahn bfs algo & cant be solved by dfs topo : Minimum Height Trees

🚀🚀🚀🚀 adj graph should be opposite i,e usually we have a->b, c->b i,e i,e we can go from a to b, but here we use b->a,c which means for going to b we need to go to a & c
        whoever indegree would be 0 we can go directlly without going anywhere.


void bfs(int s){
    queue<int> q; 
    vi indegree(n+3); 
    forr(i,s,n)
          for(auto j:g[i]) indegree[j]++;  

    forr(i,s,n) if(indegree[i]==0) q.push(i);   // Since any node with indegree 0 can start topological ordering.So we can have multiple topos.
    
    int cnt = 0;
    while(q.size()){
        int c=q.front(); 
        q.pop();
        cnt++; // To store topological order : topo.pb(c); 
        for(auto i:g[c]){
            indegree[i]--;     // Since c is done remove 1 dependency from all nodes connected to c
            if(indegree[i]==0) {  // No node is left which has to visited before visiting this.So we will visit this node now.
                q.push(i); 
            }
        }
    }
    if(cnt!=n)cout<<"cycle";  
}

