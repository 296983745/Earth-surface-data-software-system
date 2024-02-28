#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Repetition -> test111
@IDE    ：PyCharm
@Author ：haomengqi
@Date   ：2023/11/10 17:04
@Desc   ：
=================================================='''
from transformers import AutoTokenizer, AutoModel
import torch
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
from content.content_yuyi.simi_yuxian import get_mysql_list
# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained("D:\\01study\\text2vec-base")
model = AutoModel.from_pretrained("D:\\01study\\text2vec-base")
def simichnzn(sen1, sen2):
    # Tokenize sentences
    encoded_input = tokenizer([sen1, sen2], padding=True, truncation=True, return_tensors='pt')

    # Compute token embeddings
    with torch.no_grad():
        model_output = model(**encoded_input)

    # Perform pooling. In this case, mean pooling.
    sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

    normalized_vector1 = torch.nn.functional.normalize(sentence_embeddings[0].unsqueeze(0), dim=1)
    normalized_vector2 = torch.nn.functional.normalize(sentence_embeddings[1].unsqueeze(0), dim=1)

    # 计算余弦相似度
    similarity = torch.nn.functional.cosine_similarity(normalized_vector1, normalized_vector2)

    return similarity.item()



sentences = ["sentence1"]
embeddings = simichnzn(sentences[0],sentences[0])
print(sentences[0])
print(embeddings)