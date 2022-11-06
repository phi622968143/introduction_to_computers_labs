import os

dir=list(os.getcwd().split(os.path.sep))
dirs=list(os.listdir())
print(dir)
print(dirs)
path = 'f54101056.txt'
f = open(path, 'w')
for listitem in dir:
    f.write('%s\n' % listitem)
f.write(os.linesep)#wow os.linesep 在這有用 "\n" 爛掉了
for listitem in dirs:
    f.write('%s\n' % listitem)
f.close()

