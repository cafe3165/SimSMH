from stanfordcorenlp import StanfordCoreNLP

    # print(index)
# for i in resulSet4:
#
#     print(i.split('if'))
# print(resulSet4_action)
# print(resulSet4_if)


def dealResulSet4(resulSet4):
    nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )
    resulSet4_if = []
    resulSet4_action = []

    for i in resulSet4:
        print(i)
        pl = nlp.pos_tag(i)
        index = 0
        for j in pl:
            if (j[0] == 'if'):
                break
            else:
                index += 1
        if (index > 0):
            ll = i.split(' if')
            If = 'if' + ll[1]
            resulSet4_if.append(If.replace('.', ''))
            Action = ll[0]
            resulSet4_action.append(Action.replace('.', ''))
        else:
            ll = i.split(',')
            If = ll[0]
            resulSet4_if.append(If.replace('.', ''))
            Action = ll[1]
            resulSet4_action.append(Action.replace('.', ''))

    nlp.close()
    Set4=[]
    Set4.append(resulSet4_if,resulSet4_action)

    return Set4