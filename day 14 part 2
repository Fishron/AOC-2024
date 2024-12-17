X=[[*map(int,"".join(el for el in e.rstrip()if el not in"pv=").replace(","," ").split())]for e in open(0)]
n,m=103,101

def f(grid):
    n,m=len(grid),len(grid[0])
    s=set()
    for i in range(n):
        for j in range(m):
            if grid[i][j]and (i,j)not in s:
                val=0
                ns={(i,j)}
                q=[(i,j)]
                mi=inf
                Mi=-inf
                mj=inf
                Mj=-inf
                while q:
                    xi,xj=q.pop()
                    mi=[mi,xi][xi<mi]
                    mj=[mj,xj][xj<mj]
                    Mi=[Mi,xi][xi>Mi]
                    Mj=[Mj,xj][xj>Mj]
                    val+=grid[xi][xj]
                    for vi,vj in [(xi+1,xj),(xi-1,xj),(xi,xj+1),(xi,xj-1),(xi-1,xj-1),(xi+1,xj+1),(xi-1,xj+1),(xi+1,xj-1)]:
                        if 0<=vi<n and 0<=vj<m and grid[vi][vj]and (vi,vj)not in ns:
                            ns.add((vi,vj))
                            q.append((vi,vj))
                if val<100:continue
                for ii,jj in ns:
                    if (ii,Mj-jj+mj) not in ns:
                        break
                else:
                    return True
                for ii,jj in ns:
                    if (Mi-ii+mi,jj) not in ns:
                        break
                else:
                    return True
                s|=ns
                    
    return False




for I in range(101*103):
    grid=[[0]*m for _ in range(n)]
    for px,py,vx,vy in X:
        grid[(py+vy*I)%n][(px+vx*I)%m]+=1
    
    if f(grid):
        print(I)
        exit()
