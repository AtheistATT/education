import graphviz

d = graphviz.Digraph("Test")
d.attr(label="Схема икон", fontsize="20", fontname="DejaVu Sans", labelloc="t", rankdir="LR") 
d.node_attr.update(shape='star')
d.edge('q', '2')
d.edge('q', '3')
d.edge('3', '4')
d.edge('4', '2')
d.edge('3', 'q')

d.node("f", "Кириллица", color="green", shape='square')
d.edge("f", "4")
with d.subgraph(name='cluster_legend') as c:
    c.attr(label='Легенда', fontsize='16')
    c.node('L1', 'Кириллица', color='green', shape='square', fontname='DejaVu Sans')
    c.node('L2', 'Узел 2', color='red', shape='circle')

print(d.source)
d.format = "pdf"
d.render('1.pdf', view=True)
input()
