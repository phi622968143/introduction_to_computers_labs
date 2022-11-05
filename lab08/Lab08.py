import os

dir=list(os.getwd())
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
for listitem in dirs:
    f.write('%s\n' % listitem)
f.close()
