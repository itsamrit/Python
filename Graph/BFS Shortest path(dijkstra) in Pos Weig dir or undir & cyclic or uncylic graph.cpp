//✅This code is standard BFS code.Can be modified and used as BFS in any problem
//✅If Dis betn each pair is 1, then apply this same algo but with normal queue
//✅If u need to find prim min tree or dijkstra between points i,e graph not given. Then to get all possible paths/edges, make a graph with all points connected to each other with direct edges.
//          Min cost to connect all points will be Min spanning tree i,e find mst
//✅U cant convert bfs to dfs & find shortest dis.Shortest dis can be find only by bfs/queue not by dfs
//🟩MST tree is only possible in undirected graph .Since a tree is basically undirected ascylic graph
//🟩Shortest weighted path with k distance : use normal queue instead of priority.Exact same code as dijkstra of priority except : use sizee like u do in level order traversal 
//                                           && second if(dis[i.first]>c.first+i.second)  instead of dis[c.second] .Since dis is being updated continuosly & c.first will only give shortest till previous iteration while dis may include current level iterations also,so may have more than k distan i,e no level mainted



BFS question:
            https://leetcode.com/problems/01-matrix/description/  similar to starting dfs/bfs from boundry having 0 
            https://leetcode.com/problems/flood-fill/description/
            
https://leetcode.com/problems/rotting-oranges/

Common for dfs and bfs : https://leetcode.com/problems/detonate-the-maxi chutiyap
https://leetcode.com/problems/minesweeper/description/ chityap





            patan nahi
https://leetcode.com/problems/word-ladder/solutions/
https://leetcode.com/problems/word-ladder-ii/description/
https://www.geeksforgeeks.org/problems/alien-dictionary/1
https://www.geeksforgeeks.org/problems/number-of-distinct-islands/0
https://leetcode.com/problems/path-with-minimum-effort/description/
https://leetcode.com/problems/similar-string-groups/description/
https://leetcode.com/problems/number-of-provinces/description/



https://leetcode.com/discuss/interview-question/731911/please-share-dijkstras-algorithm-questions
https://leetcode.com/discuss/general-discussion/709997/questions-based-on-articulation-points-and-bridges/799168


vi dis;
vi par;
vector<vi>path;

void bfs(int s){
    priority_queue<pii,vector<pii>,greater<pii>> pq;     //Minheap : Pops out minimum first
    dis.resize(n+3,INT_MAX);
    par.resize(n+3,-1);
    
    dis[s] = 0;
    pq.push({0,s});  ✅Always put weight 1st in pair so that pq is sorted according to weight
    while (pq.size()) {
        pair<int,int> c=pq.top();
        pq.pop();
        for(auto i:g[c]){
            if (dis[i.first] > dis[c.second] + i.second){  //🟩MEMOIZE for prim mst: logic very hard : there is no link between parent & child distance in mst
                dis[i.first] = dis[c.second] + i.second;   
                pq.push({dis[i.first], i.first});
                                                    // To find path : par[i.first]=c;
            }
        }
    }
    
// TO FIND PATH :    
//     path.resize(n+3);
//     forr(i,0,n-1){
//         int j=i;
//         while(j!=-1){
//             path[i].pb(j);
//             j=par[j];       
//         }
//         reverse(path[i].begin(),path[i].end());
//     }
}
