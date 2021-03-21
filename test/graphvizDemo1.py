from graphviz import Digraph


def test():
    g = Digraph('测试图片')
    g.node(name='X', color='red')
    g.node(name='S', color='greed')
    g.node(name='R', color='blue')
    g.edge('X', 'S', color='pink')
    g.edge('S', 'R', color='pink')
    g.view()


if __name__ == '__main__':
    test()
