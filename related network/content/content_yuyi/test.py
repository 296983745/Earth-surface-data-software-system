import math

import jieba

# 1、word_similarity计算相似度
# from word_similarity import WordSimilarity2010

# ws_tool = WordSimilarity2010()
#
# b_a = '抄袭'
# b_b = '克隆'
# sim_b = ws_tool.similarity(b_a, b_b)
# print(b_a, b_b, '相似度为', sim_b)
#

# # 2 知网计算相似度
# import OpenHowNet
# OpenHowNet.download()
# hownet_dict = OpenHowNet.HowNetDict()
# hownet_dict_advanced = OpenHowNet.HowNetDict(init_sim=True)
# print('The similarity of 苹果 and 梨 is {}.'.format(hownet_dict_advanced.calculate_word_similarity('遥感','遥感')))

# 3.
# from sentence_transformers import SentenceTransformer, util
# model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
#
# # Two lists of sentence qs
# sentences1 = ['如何更换花呗绑定银行卡',
#               'The cat sits outside',
#               'A man is playing guitar',
#               'The new movie is awesome']
#
# sentences2 = ['花呗更改绑定银行卡',
#               'The dog plays in the garden',
#               'A woman watches TV',
#               'The new movie is so great']
#
# # Compute embedding for both lists
# embeddings1 = model.encode(sentences1)
# embeddings2 = model.encode(sentences2)
#
# cosine_scores = util.cos_sim(embeddings1, embeddings2)
# print(cosine_scores)

# HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /api/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 (Caused by SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1129)')))

# cs = CilinSimilarity()
# sim = cs.sim2016('繁衍', '植被覆盖度')
# print(sim)

import re, datetime

if __name__ == '__main__':
    content = ['Hello 1234 Word_This is just a test 666 Test']

    result = re.search('(\d{4}).*?(\d{4}).*', content[0])
    print(result)
    print(result.group())  # print(result.group(0)) 同样效果字符串
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
    # import re
    #
    # content = 'Hello 123456789 Word_This is just a test 666 Test'
    # result = re.search('(\d+).*?(\d+).*', content)
    #
    # print(result)
    # print(result.group())  # print(result.group(0)) 同样效果字符串
    # print(result.groups())
    # print(result.group(1))
    # print(result.group(2))