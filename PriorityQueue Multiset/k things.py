//Tc=o(n*logn=> n*logk)  n for loop and logk for sorting caz there are only k elements in heap
✅✅ 👉 Maxheap(priority_queue<int>pq) pops maximum element & similarly minheap pops out mininum. Minheap : priority_queue<int,vector<int>,greater<int>>pq; 



def kth_largest_elements(arr, k):
    ans = []
    minheap = []                                        

    for num in arr:
        heapq.heappush(minheap, num)               #For maxheap : heappush(maxheap, -num)
        if len(minheap) > k:
            ans.append(heapq.heappop(minheap))  

    while minheap:
        ans.append(heapq.heappop(minheap))

    return ans


Greedy : Further building you can reach with k ladders and m bricks.By using ladder u can go to any height.1st push for(i=0 to k) push all elements in pq and assume all climed by ladder then insert for(i=k to n) remove all min element so that they are climed by bricks. If bricks are over, than this is the building where we can reach.
Top k most frequent element Frequency sort: map[i]++;  minheap.push({i->second,i->first});
Print k closest numbers to given number: priority_queue<pair<int,int>>  and  maxheap.push({abs(arr[i]-x),arr[i]});
Print k closest points from origin:  priority_queue<pair<int, pair<int,int>>maxheap;    maxheap.push({arr[i][0]*arr[i][0]+arr[i][1]*arr[i][1] , {arr[i][0],arr[i][1]}};   //dis of point (x,y) from (0,0)=root(x^2 +y^2)

