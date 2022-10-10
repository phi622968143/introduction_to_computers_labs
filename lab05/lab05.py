dict0={ "index":["國文", "英文", "數學", "自然", "社會"]
        ,"StuA":[50, 60, 70, 80, 90]
        ,"StuB":[57, 86, 73, 82, 43]
        ,"StuC":[97, 96, 86, 97, 83]
}#remember to use ',' to seperate lists
print(dict0)
#use key to print value,int cast for divide
print("A學生平均成績:",int(sum(dict0["StuA"])/5))
print("B學生平均成績:",int(sum(dict0["StuB"])/5))
print("C學生平均成績:",int(sum(dict0["StuC"])/5))

item=list(dict0.values())
for j in range(0,5):
	sums=0
	for i in range(1,4):
		sums+=item[i][j]
		if (i==3):
			print(item[0][j],"平均成績:",sums/3)	

