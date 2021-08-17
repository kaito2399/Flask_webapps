import itertools
import numpy as np
def haibun(O,A):
    n=len(O)
    min_sa=float('inf')
    for c in itertools.combinations(range(A-1),n-1):
        haibun={}
        for i in range(n):
            if i==0:
                haibun[float(O[i])]=(c[0]+1)
            elif i==n-1:
                haibun[float(O[i])]=(A-1-c[-1])
            else:
                haibun[float(O[i])]=(c[i]-c[i-1])
        sa=sum([(i*haibun[i]-j*haibun[j])**2 for (i,j) in itertools.combinations(haibun,2)])
        if sa<min_sa:
            min_sa=sa
            min_haibun=haibun
            hm=[i*haibun[i] for i in haibun]
    if min(hm)<A:
        return 'トリガミ',min_haibun, hm
    else:
        return 'Optimal!', min_haibun, hm

def haibun3(O,A):
    n=len(O)
    haibun=[]
    for i in O:
        if A%i==0:
            haibun.append(A//i)
        else:
            haibun.append(A//i+1)
    if sum(haibun)>A:
        hm=[haibun[i]*O[i] for i in range(n)]
        return 'トリガミ',haibun, hm
    else:
        nokori=A-int(sum(haibun))
        print(nokori)
        for i in range(nokori):
            vs={}
            for j in range(n):
                haibun[j]+=1
                hm=[haibun[i]*O[i] for i in range(n)]
                v=np.var(hm)
                vs[j]=v
                haibun[j]-=1
            min_v=min(vs, key=vs.get)
            haibun[min_v]+=1
        hm=[haibun[i]*O[i] for i in range(n)]
        min_haibun={O[i]:haibun[i] for i in range(n)}
        return 'Optimal!',min_haibun, hm 

    