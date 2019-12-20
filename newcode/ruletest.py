# coding = 'utf-8'
# -- coding: utf-8 -


from stanfordcorenlp import StanfordCoreNLP
from py2neo import Graph, Node, Relationship, RelationshipMatcher

graph = Graph("bolt://127.0.0.1:7687", username='neo4j', password='123456')
nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05')


def f(sentence):
    # print(nlp.parse(line))
    denpar_list=nlp.dependency_parse(sentence)
    word_list = nlp.pos_tag(sentence)
    print(denpar_list)
    print(word_list)
    # for par in denpar_list:
    #     vb_index = par[2]
    #     if word_list[par[2] - 1][1] == 'VB':
    #         vb_beg = word_list[par[2] - 1][0]
    #         # print(vb_beg)
    #
    #         for par1 in denpar_list:
    #             if par1[0] == 'compound:prt' and par1[1] == par[2]:
    #                 vb_end = word_list[par1[2] - 1][0]
    #                 # print(vb_end)

    for d in denpar_list:
        print(d[0],d[1],d[2])
    # for w in word_list:

    return


line = "if the temperature in the sitting room is below x"

f(line)

# file=open("Rule.txt")
# for i in file:
    # print(i)
    # f(i)


