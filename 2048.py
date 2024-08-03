import random
x=0#随机数位置
y=0#随机数
z=0#决定
hjkl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x=random.randint(0,15)
y=random.randint(1,2)*2
del hjkl[x]
hjkl.insert(x,y)
h=[hjkl[0],hjkl[1],hjkl[2],hjkl[3]]
j=[hjkl[4],hjkl[5],hjkl[6],hjkl[7]]
k=[hjkl[8],hjkl[9],hjkl[10],hjkl[11]]
l=[hjkl[12],hjkl[13],hjkl[14],hjkl[15]]
v=[hjkl[0],hjkl[4],hjkl[8],hjkl[12]]
b=[hjkl[1],hjkl[5],hjkl[9],hjkl[13]]
n=[hjkl[2],hjkl[6],hjkl[10],hjkl[14]]
m=[hjkl[3],hjkl[7],hjkl[11],hjkl[15]]
print(h)
print(j)
print(k)
print(l)
while 0 in hjkl:
    z=int(input(""))
    if z==1:
        #v
        while 0 in v:
            del v[v.index(0)]
        if len(v)>1:
            if v[0]==v[1]:
                v.insert(0,v[0]*2)
                del v[1]
                del v[1]
                if len(v)>2:
                    if v[1]==v[2]:
                        v.insert(1,v[1]*2)
                        del v[2]
                        del v[2]
            elif len(v)>2:
                if v[1]==v[2]:
                    v.insert(1,v[1]*2)
                    del v[2]
                    del v[2]
                elif len(v)>3:
                    if v[2]==v[3]:
                        v.insert(2,v[2]*2)
                        del v[3]
                        del v[3]
        #b
        while 0 in b:
            del b[b.index(0)]
        if len(b)>1:
            if b[0]==b[1]:
                b.insert(0,b[0]*2)
                del b[1]
                del b[1]
                if len(b)>2:
                    if b[1]==[2]:
                        b.insert(1,b[1]*2)
                        del b[2]
                        del b[2]
            elif len(b)>2:
                if b[1]==b[2]:
                    b.insert(1,b[1]*2)
                    del b[2]
                    del b[2]
                elif len(b)>3:
                    if b[2]==b[3]:
                        b.insert(2,b[2]*2)
                        del b[3]
                        del b[3]
        #n
        while 0 in n:
            del n[n.index(0)]
        if len(n)>1:
            if n[0]==n[1]:
                n.insert(0,n[0]*2)
                del n[1]
                del n[1]
                if len(n)>2:
                    if n[1]==n[2]:
                        n.insert(1,n[1]*2)
                        del n[2]
                        del n[2]
            elif len(n)>2:
                if n[1]==n[2]:
                    n.insert(1,n[1]*2)
                    del n[2]
                    del n[2]
                elif len(n)>3:
                    if n[2]==n[3]:
                        n.insert(2,n[2]*2)
                        del n[3]
                        del n[3]
        #m
        while 0 in m:
            del m[m.index(0)]
        if len(m)>1:
            if m[0]==m[1]:
                m.insert(0,m[0]*2)
                del m[1]
                del m[1]
                if len(m)>2:
                    if m[1]==m[2]:
                        m.insert(1,m[1]*2)
                        del m[2]
                        del m[2]
            elif len(m)>2:
                if m[1]==m[2]:
                    m.insert(1,m[1]*2)
                    del m[2]
                    del m[2]
                elif len(m)>3:
                    if m[2]==m[3]:
                        m.insert(2,m[2]*2)
                        del m[3]
                        del m[3]
    elif z==2:
        v.reverse() 
        b.reverse()
        n.reverse()
        m.reverse()
        #v
        while 0 in v:
            del v[v.index(0)]
        if len(v)>1:
            if v[0]==v[1]:
                v.insert(0,v[0]*2)
                del v[1]
                del v[1]
                if len(v)>2:
                    if v[1]==v[2]:
                        v.insert(1,v[1]*2)
                        del v[2]
                        del v[2]
            elif len(v)>2:
                if v[1]==v[2]:
                    v.insert(1,v[1]*2)
                    del v[2]
                    del v[2]
                elif len(v)>3:
                    if v[2]==v[3]:
                        v.insert(2,v[2]*2)
                        del v[3]
                        del v[3]
        #b
        while 0 in b:
            del b[b.index(0)]
        if len(b)>1:
            if b[0]==b[1]:
                b.insert(0,b[0]*2)
                del b[1]
                del b[1]
                if len(b)>2:
                    if b[1]==[2]:
                        b.insert(1,b[1]*2)
                        del b[2]
                        del b[2]
            elif len(b)>2:
                if b[1]==b[2]:
                    b.insert(1,b[1]*2)
                    del b[2]
                    del b[2]
                elif len(b)>3:
                    if b[2]==b[3]:
                        b.insert(2,b[2]*2)
                        del b[3]
                        del b[3]
        #n
        while 0 in n:
            del n[n.index(0)]
        if len(n)>1:
            if n[0]==n[1]:
                n.insert(0,n[0]*2)
                del n[1]
                del n[1]
                if len(n)>2:
                    if n[1]==n[2]:
                        n.insert(1,n[1]*2)
                        del n[2]
                        del n[2]
            elif len(n)>2:
                if n[1]==n[2]:
                    n.insert(1,n[1]*2)
                    del n[2]
                    del n[2]
                elif len(n)>3:
                    if n[2]==n[3]:
                        n.insert(2,n[2]*2)
                        del n[3]
                        del n[3]
        #m
        while 0 in m:
            del m[m.index(0)]
        if len(m)>1:
            if m[0]==m[1]:
                m.insert(0,m[0]*2)
                del m[1]
                del m[1]
                if len(m)>2:
                    if m[1]==m[2]:
                        m.insert(1,m[1]*2)
                        del m[2]
                        del m[2]
            elif len(m)>2:
                if m[1]==m[2]:
                    m.insert(1,m[1]*2)
                    del m[2]
                    del m[2]
                elif len(m)>3:
                    if m[2]==m[3]:
                        m.insert(2,m[2]*2)
                        del m[3]
                        del m[3]
    elif z==3:
        #h
        while 0 in h:
            del h[h.index(0)]
        if len(h)>1:
            if h[0]==h[1]:
                h.insert(0,h[0]*2)
                del h[1]
                del h[1]
                if len(h)>2:
                    if h[1]==h[2]:
                        h.insert(1,h[1]*2)
                        del h[2]
                        del h[2]
            elif len(h)>2:
                if h[1]==h[2]:
                    h.insert(1,h[1]*2)
                    del h[2]
                    del h[2]
                elif len(h)>3:
                    if h[2]==h[3]:
                        h.insert(2,h[2]*2)
                        del h[3]
                        del h[3]
        #j
        while 0 in j:
            del j[j.index(0)]
        if len(j)>1:
            if j[0]==j[1]:
                j.insert(0,j[0]*2)
                del j[1]
                del j[1]
                if len(j)>2:
                    if j[1]==j[2]:
                        j.insert(1,j[1]*2)
                        del j[2]
                        del j[2]
            elif len(j)>2:
                if j[1]==j[2]:
                    j.insert(1,j[1]*2)
                    del j[2]
                    del j[2]
                elif len(j)>3:
                    if j[2]==j[3]:
                        j.insert(2,j[2]*2)
                        del j[3]
                        del j[3]
        #k
        while 0 in k:
            del k[k.index(0)]
        if len(k)>1:
            if k[0]==k[1]:
                k.insert(0,k[0]*2)
                del k[1]
                del k[1]
                if len(k)>2:
                    if k[1]==k[2]:
                        k.insert(1,k[1]*2)
                        del k[2]
                        del k[2]
            elif len(k)>2:
                if k[1]==k[2]:
                    k.insert(1,k[1]*2)
                    del k[2]
                    del k[2]
                elif len(k)>3:
                    if k[2]==k[3]:
                        k.insert(2,k[2]*2)
                        del k[3]
                        del k[3]
        #l
        while 0 in l:
            del l[l.index(0)]
        if len(l)>1:
            if l[0]==l[1]:
                l.insert(0,l[0]*2)
                del l[1]
                del l[1]
                if len(l)>2:
                    if l[1]==l[2]:
                        l.insert(1,l[1]*2)
                        del l[2]
                        del l[2]
            elif len(l)>2:
                if l[1]==l[2]:
                    l.insert(1,l[1]*2)
                    del l[2]
                    del l[2]
                elif len(l)>3:
                    if l[2]==l[3]:
                        l.insert(2,l[2]*2)
                        del l[3]
                        del l[3]
    else:
        z=4
        h.reverse() 
        j.reverse()
        k.reverse()
        l.reverse()
        #h
        while 0 in h:
            del h[h.index(0)]
        if len(h)>1:
            if h[0]==h[1]:
                h.insert(0,h[0]*2)
                del h[1]
                del h[1]
                if len(h)>2:
                    if h[1]==h[2]:
                        h.insert(1,h[1]*2)
                        del h[2]
                        del h[2]
            elif len(h)>2:
                if h[1]==h[2]:
                    h.insert(1,h[1]*2)
                    del h[2]
                    del h[2]
                elif len(h)>3:
                    if h[2]==h[3]:
                        h.insert(2,h[2]*2)
                        del h[3]
                        del h[3]
        #j
        while 0 in j:
            del j[j.index(0)]
        if len(j)>1:
            if j[0]==j[1]:
                j.insert(0,j[0]*2)
                del j[1]
                del j[1]
                if len(j)>2:
                    if j[1]==j[2]:
                        j.insert(1,j[1]*2)
                        del j[2]
                        del j[2]
            elif len(j)>2:
                if j[1]==j[2]:
                    j.insert(1,j[1]*2)
                    del j[2]
                    del j[2]
                elif len(j)>3:
                    if j[2]==j[3]:
                        j.insert(2,j[2]*2)
                        del j[3]
                        del j[3]
        #k
        while 0 in k:
            del k[k.index(0)]
        if len(k)>1:
            if k[0]==k[1]:
                k.insert(0,k[0]*2)
                del k[1]
                del k[1]
                if len(k)>2:
                    if k[1]==k[2]:
                        k.insert(1,k[1]*2)
                        del k[2]
                        del k[2]
            elif len(k)>2:
                if k[1]==k[2]:
                    k.insert(1,k[1]*2)
                    del k[2]
                    del k[2]
                elif len(k)>3:
                    if k[2]==k[3]:
                        k.insert(2,k[2]*2)
                        del k[3]
                        del k[3]
        #l
        while 0 in l:
            del l[l.index(0)]
        if len(l)>1:
            if l[0]==l[1]:
                l.insert(0,l[0]*2)
                del l[1]
                del l[1]
                if len(l)>2:
                    if l[1]==l[2]:
                        l.insert(1,l[1]*2)
                        del l[2]
                        del l[2]
            elif len(l)>2:
                if l[1]==l[2]:
                    l.insert(1,l[1]*2)
                    del l[2]
                    del l[2]
                elif len(l)>3:
                    if l[2]==l[3]:
                        l.insert(2,l[2]*2)
                        del l[3]
                        del l[3]
    while len(h)<4:
        h.append(0)
    while len(j)<4:
        j.append(0)
    while len(k)<4:
        k.append(0)
    while len(l)<4:
        l.append(0)
    while len(v)<4:
        v.append(0)
    while len(b)<4:
        b.append(0)
    while len(n)<4:
        n.append(0)
    while len(m)<4:
        m.append(0)
    if z==4:
        h.reverse() 
        j.reverse()
        k.reverse()
        l.reverse()
    if z==2:
        v.reverse() 
        b.reverse()
        n.reverse()
        m.reverse()
    if z==3 or z==4:
        for i in range(0,4):
            hjkl[i]=h[i]
        for i in range(0,4):
            hjkl[i+4]=j[i]
        for i in range(0,4):
            hjkl[i+8]=k[i]
        for i in range(0,4):
            hjkl[i+12]=l[i]
    else:
        for i in range(0,4):
            hjkl[i*4]=v[i]
        for i in range(0,4):
            hjkl[i*4+1]=b[i]
        for i in range(0,4):
            hjkl[i*4+2]=n[i]
        for i in range(0,4):
            hjkl[i*4+3]=m[i]
    x=random.randint(0,15)
    while hjkl[x]!=0:
        x=random.randint(0,15)
    y=random.randint(1,2)*2
    del hjkl[x]
    hjkl.insert(x,y)
    c=hjkl
    h=[hjkl[0],hjkl[1],hjkl[2],hjkl[3]]
    j=[hjkl[4],hjkl[5],hjkl[6],hjkl[7]]
    k=[hjkl[8],hjkl[9],hjkl[10],hjkl[11]]
    l=[hjkl[12],hjkl[13],hjkl[14],hjkl[15]]
    v=[hjkl[0],hjkl[4],hjkl[8],hjkl[12]]
    b=[hjkl[1],hjkl[5],hjkl[9],hjkl[13]]
    n=[hjkl[2],hjkl[6],hjkl[10],hjkl[14]]
    m=[hjkl[3],hjkl[7],hjkl[11],hjkl[15]]
    print(h)
    print(j)
    print(k)
    print(l)


