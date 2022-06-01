# (Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105




def fun(a):
    i=0
    b=[]
    while i<len(a):
        d=str(a[i])
        c=" "
        j=0
        while j<len(d):
            if d[j]!="0":
                c=c+d[j]
            j=j+1
        b.append(int(c))
        i=i+1
    print(b)
fun([1450,96000,1050,-1050])  
# mistake solution