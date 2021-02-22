print('Imported my_module')
test = "Love"
def find_index(to_search, target):
    '''Encuentra el índice de un valor en una secuencia'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
