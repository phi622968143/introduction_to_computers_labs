def gcd(a, b):
    if (a==0)or(b==0):
        print("0 沒有gcd")
        return
    #set num to be modded
    elif a>b:
        max=a
        min=b
    else:
        max=b
        min=a
    
    while(max%min!=0):
        r=max%min
        max=min
        min=r    

    if min==1:
        print(a,"和",b,"互質")
    else:
        print(a,"和",b,"的gcd=",min)

gcd(80, 20)
gcd(10, 0)
gcd(19, 20)
