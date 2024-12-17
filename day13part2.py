from math import gcd,lcm
X=[e.rstrip()for e in open(0)if e!="\n"]
n=len(X)

def direction(A):
    gc=gcd(*A)
    return [e//gc for e in A]

def bezout(a,b):
    r,u,v=a,1,0
    R,U,V=b,0,1
    while R!=0:
        x=r//R
        r,u,v,R,U,V=R,U,V,r-x*R,u-x*U,v-x*V
    return r,u,v
o=0
BIG=10000000000000

for i in range(0,n-2,3):
    l1,l2,l3=X[i:i+3]
    v1,v2=l1.split(",")
    A=[int(v1[v1.find("+")+1:]),int(v2[v2.find("+")+1:])]
    v1,v2=l2.split(",")
    B=[int(v1[v1.find("+")+1:]),int(v2[v2.find("+")+1:])]
    
    v1,v2=l3.split(",")
    tar=[int(v1[v1.find("=")+1:])+BIG,int(v2[v2.find("=")+1:])+BIG]
    
    if tar[0]%gcd(A[0],B[0]) or tar[1]%gcd(A[1],B[1]):
        continue

    #B vector line containing tar ax+by+c==0
    a=-B[1]
    b=B[0]
    c=-a*tar[0]-b*tar[1]
    def f(x,y):
        return a*x+b*y+c
    
    if f(0,0)==0:
        if direction(A)==direction(B)==direction(tar):
            cur=0
            gc,u,v=bezout(A[0],B[0])
            lc=lcm(A[0],B[0])
            nb=tar[0]//gc
            Aused=nb*u
            Bused=nb*v
            equiA=lc//A[0]
            equiB=lc//B[0]
            disc=3*equiA-equiB
            
            if disc>=0:
                #take as few As as possible
                lo=-nb*max(u,v)-1
                hi=nb*max(u,v)+1
                while hi-lo>1:
                    mid=(lo+hi)//2
                    if Aused+equiA*mid>=0:
                        hi=mid
                    else:
                        lo=mid
                Aused+=equiA*hi
                Bused-=equiB*hi
                if Bused<0:
                    continue
            else:
                #takes as few Bs as possible
                lo=-nb*max(u,v)-1
                hi=nb*max(u,v)+1
                while hi-lo>1:
                    mid=(lo+hi)//2
                    if Bused+equiB*mid>=0:
                        hi=mid
                    else:
                        lo=mid
                Aused-=equiA*hi
                Bused+=equiB*hi
                if Aused<0:
                    continue
            o+=Aused*3+Bused
        elif direction(A)==direction(tar) and tar[0]%A[0]==0:
            o+=3*tar[0]//A[0] 
        elif direction(B)==direction(tar) and tar[0]%B[0]==0:
            o+=tar[0]//B[0]
    else:
        lo=-1
        hi=BIG*2
        if f(0,0)>0:        

            while hi-lo>1:
                mid=(lo+hi)//2
                candx=A[0]*mid
                candy=A[1]*mid
                if f(candx,candy)<=0:
                    hi=mid
                else:
                    lo=mid
        else:

            while hi-lo>1:
                mid=(lo+hi)//2
                candx=A[0]*mid
                candy=A[1]*mid
                if f(candx,candy)>=0:
                    hi=mid
                else:
                    lo=mid
        if hi==BIG*2:continue
        if A[0]*hi<=tar[0] and f(A[0]*hi,A[1]*hi)==0 and (tar[0]-A[0]*hi)%B[0]==0:
            o+=hi*3+(tar[0]-A[0]*hi)//B[0]
        
            
        
print(o)