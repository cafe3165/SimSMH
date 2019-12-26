# coding:utf-8
from py2neo import Graph, Node, Relationship, RelationshipMatcher,NodeMatcher

graph = Graph("bolt://127.0.0.1:7687", username='neo4j', password='123456' )



# a = Node('Person', name='fengling')
# b = Node('Person', name='yingying')
# graph.create(a)
# graph.create(b)
# r = Relationship(a, 'KNOWS', b)
# print(a, b , r)

# print(graph.run("MATCH (a:Person) RETURN a.name").data()[2])
matcher=NodeMatcher(graph)

people=len(matcher.match(name="fengling"))
print(people)
