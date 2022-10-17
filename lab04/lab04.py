A=[]

B=[]

C=[]

subjects=['國文','英文','數學','自然','社會']

print("請依序輸A同學成績(國文 英文 數學 自然 社會):")

for n in range(0,5):

    A.append(int(input()))

n=0

print("A同學成績:")

while(n<5):

    if n==4:

        print(subjects[n]+":"+str(A[n]))

    else:

        print(subjects[n]+":"+str(A[n])+"、",end='')

    n+=1 

print("請依序輸入B同學成績(國文 英文 數學 自然 社會):")

for n in range(0,5):

    B.append(int(input()))

n=0

print("B同學成績:")

while(n<5):

    if n==4:

        print(subjects[n]+":"+str(B[n]))

    else:

        print(subjects[n]+":"+str(B[n])+"、",end='')

    n+=1 

print("請依序輸入C同學成績(國文 英文 數學 自然 社會):")

for n in range(0,5):

    C.append(int(input()))

n=0

print("C同學成績:")

while(n<5):

    if n==4:

        print(subjects[n]+":"+str(C[n]))

    else:

        print(subjects[n]+":"+str(C[n])+"、",end='')

    n+=1 

suma=0

sumb=0

sumc=0

for i in A:

    suma+=i

print("A同學平均成績:"+str(suma/5))

for i in B:

    sumb+=i

print("B同學平均成績:"+str(sumb/5))

for i in C:

    sumc+=i

print("C同學平均成績:"+str(sumc/5))

for n in range(0,5):

    print(subjects[n]+"平均成績:"+str((A[n]+B[n]+C[n])/3))
