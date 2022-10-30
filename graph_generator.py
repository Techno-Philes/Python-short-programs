#### Imports
from random import randint, shuffle


#### Settings
test_cases = 5
max_n = 10
min_n = 2
max_weight = 1000
min_weight = 10

 
print(test_cases)  #printing testcases


for j in range(test_cases):

    n=randint(min_n, max_n)
    m = randint(n-1, (n*n-n) // 2) 

    v=[j+1 for j in range(n)]
    shuffle(v) 

    edges=[]
    edge_map={}

    nodes=[v.pop()] 
    while (len(v)):
        k=v.pop()
        c=nodes[randint(0, len(nodes)-1)]

        if randint(0,1): 
            edges.append([c,k])
        else:
            edges.append([k,c])

        nodes.append(k)
        shuffle(nodes)

        edge_map[(c,k)]=1
        edge_map[(k,c)]=1

    for j in range(n, m+1): 
        p=randint(1, n)
        q=randint(1, n)
        
        while (p, q) in edge_map or (q,p) in edge_map or p==q:
            p=randint(1,n)
            q=randint(1,n) 
        
        if randint(0,1): 
            edges.append([p,q])
        else:
            edges.append([q,p])
 
        edge_map[(p,q)]=1
        edge_map[(q,p)]=1
 
    shuffle(edges)
    
    weights = [randint(min_weight, max_weight) for j in range(m)]

    print("Nodes: {}, Edges: {}".format(n, m)) 
    
    j = 0

    for i in edges:
        print(i[0], i[1], weights[j])
        j+=1