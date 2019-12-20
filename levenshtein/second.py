EMPTY = "_"
RESH = "#"
from asciitree import LeftAligned

PATHS = []

class Value:
    val = None
    _back = []

    def __init__(self, val, _back, *args, **kwargs):
        self.val = val
        self._back = _back

    @property
    def val(self, ):
        return self.val

    def set_val(self, val):
        self.val = val


    def __repr__(self):
        return str(self.val) +" " + str(self._back)


def setval(a, val):
    a = val

def initialize(string1, string2):
    a = list()
    for i in range(0, len(string1)):
        a.append(list())
        for j in range(0, len(string2)):
            a[i].append(Value(j- 2 + i, []))

    for i in range(0, len(string2)):
        a[0][i] = Value(string2[i], [])
        try:
            a[1][i+2] = Value(i+1, [(1,i+1),])
        except:
            pass

    for i in range(0, len(string1)):
        a[i][0] = Value(string1[i], [])
        try:
            a[i+2][1] = Value(i+1, [(i+1,1),])
        except:
            pass
    return a

def calculate_path(i, j, obj, massive):
    indexes = ((i-1, j), (i, j-1))
    values = map(lambda x: (massive[x[0]][x[1]].val + 1, x) , indexes)
    values.append((massive[i-1][j-1].val + (2 if massive[i][0].val != massive[0][j].val else 0), (i-1, j-1)))
    '''
        Get minimal number
    '''
    massive_back = (massive[i-1][j].val, massive[i][j-1].val, massive[i-1][j-1].val)
    minimal_previous = min(massive_back)

    minimal  = min(values, key=lambda x: x[0])[0]
    paths = filter(lambda x: x[0] == minimal, values)
    print paths #and minimal_previous == massive[x[1][0]][x[1][1]].val, values)
    return Value(minimal, map(lambda x: x[1], paths))

def get_path(massive, l1, l2, s=[]):
    path = (massive[l1][l2]._back[0][0], massive[l1][l2]._back[0][1])
    s.append(path);
    if path[0]!=1 or path[1]!=1:
        get_path(massive, path[0],path[1], s)
    return s


def construct_all_paths(path_item, tree, a):
    for path in path_item._back:
        tree.update({path: {}})
        construct_all_paths(a[path[0]][path[1]], tree.get(path), a)
    return tree

def algorithm(string1, string2):
    string1 = EMPTY + RESH + string1
    string2 = EMPTY + RESH + string2
    a = initialize(string1, string2)
    for i in range(2,len(string1)):
        for j in range(2,len(string2)):
            a[i][j] = calculate_path(i,j, a[i][j], a)
    path = get_path(a, len(string1)-1, len(string2)-1,)
    path_tree = construct_all_paths(a[len(string1) - 1][len(string2)- 1], {}, a)
    return path, path_tree

if __name__ == '__main__':
    str1, str2 = (raw_input(), raw_input())
    path, path_tree = algorithm(str1, str2)

    print '\nPath - '
    print path
    tr = LeftAligned()
    print tr(path_tree)

