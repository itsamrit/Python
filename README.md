if u check if node1 = node2 in linked list then not only its [val, next] pointer is checked it checks if its at the same memory block. so 

so even 2 nodes have same value and next pointer value is same like 4->3->4->3 and 2->3->5, both 4 nodes are different

https://leetcode.com/problems/linked-list-cycle/description/




when ur distance is not equl to each negihout i,e using heap for bfs than u cant have vis, since node may have shorter dis in next few steps so u use dis[] instead of vis[] for bfs heap cases

IN toposort u can use normal logic to color each traversal using one unique color  instead of 1 and 2

        adj = [[] for i in range(n)]
        vis = [0 for i in range(n)]    
        for placing on 4th position
        
ans =sorted(ans) or ans.sort() same wiht reversed and .reverse()  
        in python while loop check while condition every iteration and for loops sets value once 
 so in level order traversal while(q): for i in range(len(q)):
        

s=s[:4]+'e'+s[5:]


                        temp = str(temp)
In python to convert anything to anything just write in starting a = list(a) a = string(b) a = set(a)


💡💡💡💡Whether u have set/dict of int or strings like in word ladder or set of lists insertion, searching tc is o(1). 

💡💡MY whole thinking was wrong. set/dict uses hashtable for all not like if set of string it will have  tc = tc of set searching * word length😤

PYTHON use HASHTABLE ave tc of set/map insertion/deletion/searching is o(1) only
MASTER
EXCEPT INT ALL VISITED MARKING USING MAP/set
EVEN IF LIST OF LIST OF INT use set 
When you are delling with string like graph of words, u cant implement some crazy algo , for marking visited dont use vis[i] use set to store words and check dont thing about tc.

Only 2 things like list of int a and for matrix u can a same size list and matrix for marking vis . OTHER than that use set even if list of list of int like circle point [[0,1], [4,4]) use set.
Dont think about tc its same only. 

IN above case list because commonly used.


 For string/words problems use set for marking visited and dict for any computation like parent[word[i]] =  word[c](in word ladder 2)  u cant use list in string

 
 Basically u can mark visited using map but set looks cool but NEVER EVER TRY TO USE LIST

I am bad when even a single loop brackets comes and i just want to quit😡😡😡😡😡😡
while writing also it takes times because autocomplete not works😤😤😤 in looping and its so confusing😤😤
FOUND SPEED GOES SIGNIFICANTLY DOWN AND LOGICAL THINKING IN LOOP OF [[]] SO TRY TO AVOID 


THERE ARE MANY FLAGS U CAN PUT, REMOVE A SINGLE SOLUTION


so x= c[0] and grid[x][y] instead of grid[c[0]][c[1]]

NO PAIRS in python simple language
Certainly! Here's the equivalent code in Python for the given operations on different data types:

🥳BFS without levelorder traversal or priority could be done by dfs also. Only question that req priorityqueue or level order traversal could be done by BFS.
🥳pop for rightmost element in list(stack), queue. popleft() for leftmost in deque


🥳del a[i] for any element in list, dict(map).  .add(element).remove(element) for set

🥳ceil() and floor()

🥳dafaultdict(defaultdict(int)) for adjacenylist  g[a][b] = val  

🥳Iteration
```
for key in my_dict:
    print(key, my_dict[key])
for element in set:
    print(element)
```

in for all things just like MySQL for searching

1. Dynamic Arrays (List):
   
```python
LEEetcode python is 3.11 so by default defaultdict is ordered only
a = []
a.append(element)
last = a.pop()  //here pop returns value and pops the last elemetn   a.remove(element)    del a[index]
size = len(a)
last = a[i]
del a[i]
For appending shallow copy of list into another list
ans.append(temp.copy())
```

2. String(immutable):
```python
s = "Hello, World!"
temp = str_var
temp += 'c'   # this creates a new string with same name temp, the previous with 
size = len(str_var)
c = str_var[i]
my_string = my_string[:-1]    # Slice to exclude last character, this make new string, since string are immutable in python

For appending shallow copy of string into another list
ans.append(s)    # since string are immutable so this string is not going to be modified in future. Even if add or slice this a new string is generated with same name
```

3. Char:
```python
c = 'A'
```

5. Stack:
Python doesn't have a built-in implementation of a traditional stack. Lists in Python can be used as stacks

6. Queue(deque):

```python
Python's `deque` can be used as a double-ended queue, Python has queue but its more for complicated task not used for DSA
from collections import deque

q = deque()
q.append(element)
q.popleft()
size = len(q)
front = q[0]

deque_var = deque()
deque_var.appendleft(element)
deque_var.append(element)
deque_var.popleft()
deque_var.pop()
first = deque_var[0]
last = deque_var[-1]
size = len(deque_var)
```

8. Priority Queue (using heapq):
```python
import heapq

# Example of Min-Heap
h = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(h)
print("Min-Heap:", h)

# Example of Max-Heap (by negating values)
h = [-x for x in min_heap]
heapq.heapify(h)
print("Max-Heap:", [-x for x in h])

# Inserting into Min-Heap
heapq.heappush(h, 0)
print("After inserting 0 into Min-Heap:", h)

# Inserting into Max-Heap (by negating value)
heapq.heappush(h, -7)
print("After inserting -7 into Max-Heap:", [-x for x in h])

# Popping from Min-Heap
min_value = heapq.heappop(h)
print(f"Popped from Min-Heap: {min_value}, Updated Min-Heap: {h}")

# Popping from Max-Heap (by negating value)
max_value = -heapq.heappop(h)
print(f"Popped from Max-Heap: {max_value}, Updated Max-Heap: {[-x for x in h]}")

```

9. Map (Dictionary):
```python
m = defaultdict(int) #Unordered (value datatype inside small bracket)
#In python u give the parent datastruture i,e if u want in verticalorder traversal map of list of int , u give defaultdict(list)
m = {}  # m = defaultdict(int) is orderedmap used in vertical order traversal of tree
m[key] = value
del m[key]
size = len(m)
if key in m:
    value = m[key]
```

10. Set:
```python
s = set()
For converiont of list to set : s= set(listName)
s.add("Element1")
s.remove("Element2")
size = len(s)
iterator = iter(s)
if next(iterator, None) is not None:
    first_element = next(iterator)
if target_element in s:
    # Do something



5. Stack:
Python doesn't have a built-in implementation of a traditional stack. Lists in Python can be used as stacks
```








Certainly! Here's the equivalent code in Python for the given operations on different data types:


in for all things just like MySQL for searching





```

8. Priority Queue (using heapq):
```python
import heapq

# Example of Min-Heap
min_heap = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(min_heap)
print("Min-Heap:", min_heap)

# Example of Max-Heap (by negating values)
max_heap = [-x for x in min_heap]
heapq.heapify(max_heap)
print("Max-Heap:", [-x for x in max_heap])

# Inserting into Min-Heap
heapq.heappush(min_heap, 0)

# Inserting into Max-Heap (by negating value)
heapq.heappush(max_heap, -7)

# Popping from Min-Heap
min_value = heapq.heappop(min_heap)

# Popping from Max-Heap (by negating value)
max_value = -heapq.heappop(max_heap)

```

9. Map (Dictionary):
```python

m = defaultdict(int) #defauldict is part of normal dict i,e m={} which was made to solve keyerror problem. So both are ORDERED if u are using python 3.7 or above else unordered
m[key] = value
m.pop(key)
size = len(m)
if key in m:
    value = m[key]


m = OrderedDict() # u need to handle keyerror i,e if(key not in m) m[key]=0 else: m+=1
```

10. Set:
```python
s = set()
s= set(listName)
s.add("Element1")
s.remove("Element2")
size = len(s)
iterator = iter(s)
if next(iterator, None) is not None:
    first_element = next(iterator)
if target_element in s:
    # Do something
```

Note: Python dictionaries can be used as maps.




describe how to declare, add , remove and determine size in  java  of following datatypes array , dynamic array , string , char , stack , queue, deque, priority queue, map

```
🟢😊 c++ over python because, u need to explain what is array in commment instead directly write in cpp as vector
      Similar to java , i,e spring boot
      No multiple library , only bits 
      No priority queue hard. 
      Majority leetcode in cpp
      mcq of coding round
      public,protected, private already written 
      
🟢😊😒😒 Always always analyze the time complexity.
If its 10^4 or 10^5, there is high chance it uses map or set nlogn

🟢max/min between any number of arguments :  int a= max({a,b,c});

🟢Learn the techniques of all question which method will be used so that even implementation fails,u get points

🟢For online round :

To convert int to long long : long long new= (long long)old;  & vice versa i,e int new = (int)old;

int to string : to_string(num);

string to int : stoi(str);

char to int & int to char : -'0' - 'a' respectively

Size of string is not in int when applying max,min function

(int)forbidden[i].size()

🟢Only normal queue & deque has front back
  
lexographically maximum no subset more than 10 questions with different just remember it is solved by stack

👉 for(auto &i:mapp) Use &i otherwise iterator will remain on 1st element

👉 ROWs == RECORDs while column means attributes

👉In Matrix's 4 way travelling if(vis[i][j]) return; is not tle for dfs(i-1,j) & dfs(i,j-1);

BUT once rejected/deleted element for current is then rejected for all other element
IN NGR  element which is not next greater than current cant be next greater for the rest behind it

👉Thumb rule : Always intialize the queue,stack,map etc before the doing any operation on it in loops.

👉Iterators:

for(auto i:m) i.first i.second

for(auto i=m.begin(); i!=m.end(); i++) m

👉 If 2 or more arrays or numbers in questions for comparision like A & B.

Always make 1 smaller if(A>B) swap(A,B) & then solve accordingly.

👉 Never do modulo as %10^7+7 [Error]. Instead do %1000007

👉lower_bound(v.begin(),v.end(),val) gives index of 1st occurence of val if present
