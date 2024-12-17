X=[e.rstrip().replace("#","##").replace("O","[]").replace(".","..").replace("@","@.")for e in open(0)]
grid=[]
for i,e in enumerate(X):
    if "@"in e:
        sj=e.find("@")
        si=i
    if e!="":
        grid+=[*e],
    else:
        break
        
moves=[]
for e in X[i+1:]:
    moves+=list(e)


n,m=len(grid),len(grid[0])

def vois(i,j,di,dj):
    if grid[i][j]=="[":
        return [(i+di,j),(i,j+1),(i,j+dj)]
    elif grid[i][j]=="]":
        return [(i+di,j),(i,j-1),(i,j+dj)]
def area(i,j,di,dj):
    q=[(i,j)]
    s={(i,j)}
    while q:
        xi,xj=q.pop()
        if grid[xi][xj]=="#":
            return False
        for vi,vj in vois(xi,xj,di,dj):
            if (vi,vj)not in s and grid[vi][vj]in"#[]":
                    s.add((vi,vj))
                    q.append((vi,vj))
    return s
d={">":(0,1),"^":(-1,0),"v":(1,0),"<":(0,-1)}
cur=0
for mv in moves:

    cur+=1
    di,dj=d[mv]
    if 0<=si+di<n and 0<=sj+dj<m:
        if grid[si+di][sj+dj]==".":
            grid[si][sj]="."
            si+=di
            sj+=dj
            grid[si][sj]="@"
        else:
            A=area(si+di,sj+dj,di,dj)
            if A:
                oldval={}
                for vi,vj in A|{(si,sj)}:
                    oldval[vi,vj]=grid[vi][vj]
                #print(oldval)
                for vi,vj in oldval:
                    grid[vi][vj]="."
                for vi,vj in oldval:
                    vi+=di
                    vj+=dj
                    grid[vi][vj]=oldval[vi-di,vj-dj]
                si+=di
                sj+=dj

o=0
for i in range(n):
    for j in range(m):
        if grid[i][j]=="[":
            o+=100*i+j
print(o)
