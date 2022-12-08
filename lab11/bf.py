import json

def BF(input):
    N = len(input)
    #初始化 min用來找最小值(利用比較) 
    min=10000
    cost=10000
    assignment=[i for i in range(N)]#給定陣列大小  
    #根據不同員工數 進行不同次數的比較(全部組合都試過) 注意工作跟員工一對一
    if N==4:
        for i in range(0,N):
            for j in range(0,N):
                for k in range(0,N):
                    for l in range(0,N):
                        if i!=j&j!=k&k!=l&l!=i:
                            cost=input[0][i]+input[1][j]+input[2][k]+input[3][l]
                        if(cost<min):
                            min=cost
                            assignment[0]=i
                            assignment[1]=j
                            assignment[2]=k
                            assignment[3]=l
    elif N==3:
        for j in range(0,N):
            for k in range(0,N):
                for l in range(0,N):
                    if j!=k&k!=l&l!=j:
                        cost=input[0][j]+input[1][k]+input[2][l]   
                    if(cost<min):
                        min=cost
                        assignment[0]=j
                        assignment[1]=k
                        assignment[2]=l                          

    elif N==2:
        assignment
        for k in range(0,N):
            for l in range(0,N):
                if k!=l:
                    cost=input[0][k]+input[1][l]
                if(cost<min):
                    min=cost
                    assignment[0]=k
                    assignment[1]=l
                           
    else:
        
        for l in range(0,N):
            cost=input[0][l]
            if(cost<min):
                min=cost
                assignment[0]=l
                            
    return min,assignment

# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # show input data and number of the Tasks
        # print(input)

        # Brute Force Algorithm

        min,assignment = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', min)
        print()
