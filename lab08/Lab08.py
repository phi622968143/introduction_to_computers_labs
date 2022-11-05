import os

dir=list(os.getcwd())
dirs=list(os.listdir())
print(dir)
print(dirs)
path = 'f54101056.txt'
f = open(path, 'w')
for listitem in dir:
    if(listitem!=os.sep):
        f.write('%s' % listitem)
    else:
        f.write("\n")#os.linesep 間距太大 我不喜歡
f.write(os.linesep)#wow os.linesep 在這有用 "\n" 爛掉了
for listitem in dirs:
    f.write('%s\n' % listitem)
f.close()
