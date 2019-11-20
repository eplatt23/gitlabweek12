#   https://github.com/eplatt23/gitlabweek12.git
#   Emmett Platt
#   ​CSCI 102 – Section D
#   Week 12 - Part B
    

def PrintOutput(a):
    a = str(a)
    print('OUTPUT', a)

def LoadFile(name):
    the_file = open(name, 'r')
    read = the_file.readlines()
    read = list(map(lambda x:x.strip(), read))
    return read
