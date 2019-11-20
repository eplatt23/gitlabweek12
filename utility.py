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

def UpdateString(first, second, count):
    empty_list = []
    the_list = list(first)
    for i in range(len(the_list)):
        if i == count:
            empty_list.append(second)
        else:
            empty_list.append(the_list[i])
    print('OUTPUT', ''.join(empty_list))
