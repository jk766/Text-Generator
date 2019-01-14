import random

sP=str(input())
words=int(input())
k=sP.split(" ")
k.append("_end_")
u=set(k)
txt=[]

def occ(x):
    count=0
    ocs=[]
    for element in x:
        for member in k:
            if member==element:
                count=count+1
        ocs.append([element,count])
        count=0
    return ocs

def next(x):
    nxts=[]
    p=-1
    for element in k:
        p=p+1
        if element == x and len(k)>=p+2:
            nxts.append(k[p+1])
    return nxts

def dedup(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    return(y)

def result(x):
    z=occ(next(x))
    z.sort(key=lambda y: int(y[1]))
    z.reverse()
    z=dedup(z)
    z.sort(key=lambda y: int(y[1]))
    z.reverse()
    #print(z)
    if z==[]:
        return z
    elif len(z)==1:
        return(z[0][0])
    elif len(z)==2:
        #v=random.randint(0,1)
        return(z[random.randint(0,1)][0])
    elif len(z)==3:
        #v=random.randint(0,2)
        return(z[random.randint(0,2)][0])
    elif len(z)>3:
        #s=random.randint(0,5)
        if random.randint(0,7) >= 5:
            #v=random.randint(3,len(z)-1)
            return(z[random.randint(3,len(z)-1)][0])
        else:
            #v=random.randint(0,3)
            return(z[random.randint(0,3)][0])


def g(x):
    res=result(x)
    #print (res)
    if len(txt)>=words:
       return txt
    if res!="_end_":   
        txt.append(res)
        return g(res)
    else:
        txt.append(random.choice(txt))
        return g(random.choice(txt))
  

txtnew=g(str(input()))
w=""
if txtnew==[]:
    txtnew=[5]
for i in txtnew:
   if i != []:
        w=w+" "+i
w=w+"."
print(w)
