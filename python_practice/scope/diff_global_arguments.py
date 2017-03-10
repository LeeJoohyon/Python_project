global_level = 100

def argument_level_add(value):
    value[0] += 30
    print('argument_level_add, value : %s' % value)


def global_level_add():
    global global_level
    global_level[0] += 30
    print('global_level_add,value : %s' % global_level)

def show_global_level():
    print('global_level : %s' % global_level)

show_global_level()
argument_level_add(global_level)
show_global_level()
global_level_add()
show_global_level()
