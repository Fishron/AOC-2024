
X=[[*map(int,e.rstrip().split(","))]for e in open(0)]
n=71

def f(x):
    
    M=[[0]*n for _ in range(n)]
    for x,y in X[:x]:
        M[y][x]=1

    q=deque([(0,0)])

    dist=0
    while q:
        x,y=q.popleft()
        if x==y==n-1:
            return True
        for vx,vy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=vx<71 and 0<=vy<71 and M[vy][vx]==0:
                M[vy][vx]=1
                q.append((vx,vy))
    return False

lo=-1
hi=len(X)+1
while hi-lo>1:
    mid=(lo+hi)//2
    if f(mid):
        lo=mid
    else:
        hi=mid
print(X[hi-1])
