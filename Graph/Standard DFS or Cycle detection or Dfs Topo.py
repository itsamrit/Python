# //🟩This code is standard DFS code & can be used for DFS in any other problem

# //[Note: Dont try to print cycle because there is algo for printing cycle on cp alogithm website but there is no question ever asked on printing cycle]


# Check Cycle in directed graph : https://leetcode.com/problems/course-schedule-ii/


from collections import defaultdict

def checkCycle(node, adj, vis, p):
    vis[node] = 1

    for it in adj[node]:
        # For undirected graph, always a checkpoint in any algo: if it == p: continue
        if vis[it] == 0:
            if checkCycle(it, adj, vis, node):
                return True
        elif vis[it] == 1:
            return True

    vis[node] = 2  # For directed. Since in undirected after running one DFS, nodes which are visited can't come again in another DFS.
                   # But in directed, in another DFS, the same nodes may come. So, to avoid nodes already visited in previous DFS in directed, we use vis[node] = 2.
    # If no cycle found, print the topological order in reverse order. Else, no topology is possible.
    topo.append(node)
    return False

def isCycle(N, adj):
    vis = [0] * N
    for i in range(N):
        if vis[i] == 0:
            if checkCycle(i, adj, vis, -1):
                return True
    return False

# Example usage:
N = 5
adj = defaultdict(list)
adj[0].append(1)
adj[1].append(2)
adj[2].append(0)
adj[1].append(3)
adj[3].append(4)

topo = []  # Assuming this list is defined before calling isCycle function
result = isCycle(N, adj)
