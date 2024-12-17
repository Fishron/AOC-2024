X=[e.rstrip()for e in open(0)]
n,m=len(X),len(X[0])
for i in range(n):
    for j in range(m):
        if X[i][j]=="S":
            si,sj=i,j
        if X[i][j]=="E":
            ti,tj=i,j

D=[(0,1),(-1,0),(0,-1),(1,0)]
sd=0
dist=defaultdict(lambda:inf)
pred=defaultdict(list)
q=[(0,si,sj,sd)]
dist[si,sj,sd]=0
s=set()
best=inf
while q:
    prio,i,j,d=heappop(q)
    if prio!=dist[i,j,d]:
        continue
    if i==ti and j==tj and prio<=best:
        best=prio
        q=[(i,j,d,-1,-1,-1)]
        while q:
            xi,xj,xd,li,lj,ld=q.pop()
            s.add((xi,xj))
            for vi,vj,vd in pred[xi,xj,xd]:
                if (vi,vj,vd)!=(li,lj,ld):
                    q.append((vi,vj,vd,xi,xj,xd))

    for idx in range(4):
        di,dj=D[idx]
        vi,vj=i+di,j+dj
        if 0<=vi<n and 0<=vj<m and X[vi][vj]!="#":
            cand=prio+1+1000*min((idx-d)%4,(d-idx)%4)
            if cand==dist[vi,vj,idx]:
                pred[vi,vj,idx]+=[(i,j,d)]
            if cand<dist[vi,vj,idx]:
                dist[vi,vj,idx]=cand
                pred[vi,vj,idx]=[(i,j,d)]
                heappush(q,(cand,vi,vj,idx)) 
                
print(len(s))
