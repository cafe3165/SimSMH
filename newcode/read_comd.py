# coding = 'utf-8'
# -- coding: utf-8 -


import time
from stanfordcorenlp import StanfordCoreNLP
from py2neo import Graph, Node, Relationship, RelationshipMatcher
import re

graph = Graph("bolt://127.0.0.1:7687", username='neo4j', password='123456')
nlp = StanfordCoreNLP(r'D:/pycharm/newsim/stanford-corenlp-full-2018-10-05')
# # load_path = 'C:/Users/more/Desktop/code/command.txt'
# # save_path = 'C:/Users/more/Desktop/code/extrac_result.txt'
# load_path = 'C:/Users/more/Desktop/学习相关/code/cmdtst.txt'
# # save_path = 'C:/Users/more/Desktop/学习相关/code/exttst.txt'
save_path = 'exttst.txt'

# def f(line):
#     dobj_1 = ''
#     dobj_index = 0
#     dobj_com = ''
#     entity1 =''
#     vb_beg = ''
#     vb_end = ''
#     vb = ''
#     first_entity_dict = {'Node': [], 'Type': ''}
#     dobj_index = 0
#     attribute = []
#     location = []
#     device = []
#     att_dev = []
#     dev_loc = []
#     isFindWP = False
#     word_list=[]
#     denpar_list = []
#
#     # print(6666)
#     # print(6666)
#     # print(6666)
#     print(nlp.word_tokenize(line))
#
#     word_list = nlp.pos_tag(line)
#     denpar_list = nlp.dependency_parse(line)
#     #查找句子中的操作,先判断句子中是否有疑问词
#     for w in word_list:
#         if w[1] == 'WP':
#             isFindWP = True
#             break
#
#     if isFindWP:
#         print("本句为查询句。")
#     else:
#         print("本句为操作句。")
#         for par in denpar_list:
#             vb_index = par[2]
#             if word_list[par[2]-1][1] == 'VB':
#                 vb_beg = word_list[par[2]-1][0]
#                 # print(vb_beg)
#
#                 for par1 in denpar_list:
#                     if par1[0] == 'compound:prt' and par1[1] == par[2]:
#                         vb_end = word_list[par1[2]-1][0]
#                         # print(vb_end)
#         if vb_beg and vb_end:
#             vb = vb_beg+' '+vb_end
#         else:
#             vb = vb_beg
#
#         #考虑当前的操作是set...to...
#         if vb == "Set":
#             vb = vb + ' ...'
#             to_num = 0
#             for num,find_to in enumerate(word_list):
#                 if find_to[0] == 'to':
#                     to_num = num
#                     break
#             for word in word_list[to_num:]:
#                 vb = vb+' '+word[0]
#         print("operate：", vb)
#
#     #查找句子中的实体和概念
#     for index, word in enumerate(word_list):
#         if word[1] == 'NN':
#             first_entity_dict = {'Node': [], 'Type': ''}
#             # print(word)
#             # print(word[0])
#             node_d = graph.nodes.match('Device', DName=word[0])
#             node_l = graph.nodes.match('Location', LName=word[0])
#
#             if node_d:
#                 # print("第一个node_d")
#                 entity1 = word[0]
#                 for node in node_d:
#                     # first_entity_dict['Node'].append(node)
#                     first_entity_dict['Node'].append(str(node))
#                 first_entity_dict['Type'] = 'Device'
#                 # print(first_entity_dict)
#                 device.append(word[0])
#
#             elif node_l:
#                 # print("第二个node")
#                 entity1 = word[0]
#                 for node in node_l:
#                     # first_entity_dict['Node'].append(node)
#                     first_entity_dict['Node'].append(str(node))
#                 first_entity_dict['Type'] = 'Location'
#                 # print(first_entity_dict)
#                 location.append(word[0])
#
#             else:
#                 # print("找组合词")
#                 for par in denpar_list:
#                     if par[0] == 'compound' or par[0] == 'amod' and par[1] == index + 1:
#                         # print("是否进入if")
#                         dobj_com = word_list[par[2] - 1][0]
#                         entity1 = dobj_com + ' ' + word[0]
#                 entity1_node_d = graph.nodes.match('Device', DName=entity1)
#                 entity1_node_l = graph.nodes.match('Location', LName=entity1)
#
#                 if entity1_node_l:
#                     for node in entity1_node_l:
#                         # first_entity_dict['Node'].append(node)
#                         first_entity_dict['Node'].append(str(node))
#                     first_entity_dict['Type'] = 'Location'
#                     location.append(entity1)
#
#                 elif entity1_node_d:
#                     for node in entity1_node_d:
#                         # first_entity_dict['Node'].append(node)
#                         first_entity_dict['Node'].append(str(node))
#                     first_entity_dict['Type'] = 'Device'
#                     device.append(entity1)
#                 else:
#                     # entity1_node_d = graph.nodes.match('Device', Key = word[0])
#                     entity1_node_s = graph.nodes.match('Service', CType = word[0])
#                     if entity1_node_s:
#                         # print("第三个node:")
#                         for node in entity1_node_d:
#                             first_entity_dict['Node'].append(str(node))
#                         first_entity_dict['Type'] = 'attribute'
#                         attribute.append(word[0])
#
#             if first_entity_dict['Node']!= None:
#                 first_entity_dict['Type']=''
#             # print(first_entity_dict['Node'])
#             # print(first_entity_dict['Type'])
#             # print('---------------------------')
#
#
#     if attribute:
#         print('attribute:',attribute)
#     else:
#         print("句子中不存在属性")
#     print("device：",device)
#     print("location：",location)
#
#
#     #查找属性与设备之间的关系
#     if attribute:
#         for attri in attribute:
#             attribute_last = attri.split(' ')[-1]
#             attri_index = 0
#             # print("attribute_last:",attribute_last)
#
#             for dev in device:
#                 device_last = dev.split(' ')[-1]
#                 dev_index = 0
#                 # print("device_last:",device_last)
#
#                 for index, word in enumerate(word_list):
#                     if word[0] == attribute_last:
#                         attri_index = index+1
#                         # print("attri_index:",attri_index)
#                     if word[0] == device_last:
#                         dev_index = index+1
#                         # print('dev_index',dev_index)
#
#                 for par in denpar_list:
#                     if par[2] == dev_index and par[1] == attri_index and par[0] == 'nmod':
#                         # print(attri,dev)
#                         attri_dev_1 = []
#                         attri_dev_1.append(attri)
#                         attri_dev_1.append(dev)
#                         att_dev.append(attri_dev_1)
#     # else:
#     #     print("不存在属性")
#
#
#     #查找设备与地点之间的关系
#     for dev in device:
#         device_last = dev.split(' ')[-1]
#         dev_index = 0
#         # print("device_last:", device_last)
#
#         for loc in location:
#             location_last = loc.split(' ')[-1]
#             loc_index = 0
#             # print("location_last:",location_last)
#
#             for index, word in enumerate(word_list):
#                 if word[0] == device_last:
#                     dev_index = index+1
#                     # print("dev_index:",dev_index)
#                 if word[0] == location_last:
#                     loc_index = index+1
#                     # print('loc_index',loc_index)
#
#             #如果当前设备有直接的nmod
#             hasdirect_nmod = False
#             for look_nmod in denpar_list:
#                 if look_nmod[1] == dev_index and look_nmod[0] == 'nmod' and word_list[look_nmod[2]-1][0] != location_last:
#                     hasdirect_nmod = True
#             if hasdirect_nmod == True:
#                 continue
#             #记录句法分析的索引
#             for par_index, par in enumerate(denpar_list):
#                 if par[2] == dev_index:
#                     dev_par_index = par_index
#                 if par[2] == loc_index:
#                     loc_par_index = par_index
#
#             isFind = False
#             n=0
#             #while(denpar_list[dev_index-1][1]!=0):
#
#             #查找当前地点节点有没有并列连词
#             if denpar_list[loc_index-1][0] == 'conj':
#                 # print("存在并列连词")
#                 # print(word_list[int(loc_par_index)])
#                 #查看并列连词
#
#                 for location_conj in location:
#                     location_conj_last = location_conj.split(' ')[-1]
#                     if location_conj_last == word_list[int(denpar_list[loc_index-1][1])-1][0]:
#                         # print(location_conj_last)
#                         # print(location_conj)
#                         for x in dev_loc:
#                             # print(x)
#                             if x[-1].split(' ')[-1] == location_conj_last:
#                                 dev_loc_1 = []
#                                 dev_loc_1.append(x[0])
#                                 dev_loc_1.append(loc)
#                                 dev_loc.append(dev_loc_1)
#
#             else:
#                 while True:
#                     n=n+1
#                     # print(n)
#                     # print("dev_index:",dev_index)
#                     #查找当前节点的子节点
#                     for x in denpar_list:
#                         if x[0] == 'nmod' and x[1] == dev_index and word_list[x[2]-1][0] == location_last:
#                             isFind = True
#                             # print(dev,loc)
#                             dev_loc_1 = []
#                             dev_loc_1.append(dev)
#                             dev_loc_1.append(loc)
#                             dev_loc.append(dev_loc_1)
#                     if isFind or n==10:
#                         # print(isFind)
#                         break
#                     else:
#                         dev_index = denpar_list[dev_index-1][1]
#
#     if attribute:
#         print("attribute-device：",att_dev)
#     print("device-location：",dev_loc)
#     #将结果写入
#     with open(save_path,"a") as rf:
#         if device:
#             rf.write("device:")
#             rf.write(str(device)+'\n')
#         else:
#             rf.write("不存在设备"+'\n')
#         if location:
#             rf.write("location:")
#             rf.write(str(location)+'\n')
#         else:
#             rf.write("不存在地点"+'\n')
#         if attribute:
#             rf.write("attribute:")
#             rf.write(str(attribute)+'\n')
#         else:
#             rf.write("不存在属性"+'\n')
#         if vb:
#             rf.write("operation:")
#             rf.write(str(vb)+'\n')
#         else:
#             rf.write("不存在操作"+'\n')
#         rf.write(line)
# file = open(load_path)
# line = file.readline()

# line="turn off the air conditioner in the sitting room."
# line="turn on the light in the sitting room."
# line="turn on the light."

line = "increase the temperature in the sitting room."
# line="Set the brightness of the Light to 25."
# line="what is the temperature in the sitting room?"
# line="what is the value of temperature of the air conditioner?"

# line="Assign the temperature of the air conditioner in the sitting room to 25"
# line="assign the temperature of the sitting room to 28 degrees."
# line="turn off the light in bedroom."
# line="turn up the temperature of air conditioner in bedroom."
# line="increase the humidity of balcony."


# print(line)
# n = 1
# print(n)
# with open(save_path, "a")as f1:
#     f1.write(str(n) + '\n')
# f(line)
#
# while line:
#     n=n+1
#     print(n)
#     # line = file.readline()
#     with open(save_path,"a")as f2:
#         f2.write(str(n)+'\n')
#     f(line)
#     break
# file.close()
