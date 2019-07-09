from stanfordcorenlp import StanfordCoreNLP
# import rwfile

nlp = StanfordCoreNLP(r'stanford-corenlp-full-2018-10-05', )


sentence = 'if the temperature is higher than x in the sitting room , turn the temperature of the air conditioner in the sitting room to x .'


print('Tokenize:', nlp.word_tokenize(sentence))
print('Part of Speech:', nlp.pos_tag(sentence))
print('Named Entities:', nlp.ner(sentence))
# print('Constituency Parsing:', nlp.parse(sentence))  # 语法树
print('Dependency Parsing:', nlp.dependency_parse(sentence))  # 依存句法