import json
def permutations(array):
    if len(array) == 0:#沒有元素的時候
        return [[]]
    if len(array) == 1:
        return [array]
    else:
        arr = []
        for i in range(len(array)):
            array[0], array[i] = array[i], array[0]#決定第一個固定的數字
            start = array[0]
            end = permutations(array[1:])#往下切陣列
            print(end)
            for x in end:
                arr.append([start]+x)#頭加尾
    return arr
def BF(input):
    N = len(input)
    a =[]
    l=[]
    sum=0
    min=10000000
    cost=input
    for i in range(N):#產生可能的排列
        a.append(i)
    l=permutations(a)
    for p in range(len(l)):
        sum=0
        for job in range(N):
            sum+=cost[job][l[p][job]]#job 跟 agent 對應,p代表第幾個組合
        if sum<min:#找最小可能
            assign=l[p]
            min=sum
    return min,assign

# main
with open('input.json', 'r') as inputFile:
    data = json.load(inputFile) # load data
    for key in data:
        input = data[key] # load each input

        # Brute Force Algorithm

        min,assignment = BF(input)

        print('Question: ' + str(key))
        print('Assignment:', assignment)
        print('Cost:', min)
        print()
