import openpyxl
from text2vec import Similarity
from torch import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import torch

from content.content_yuyi.simi_yuxian import get_mysql_list


# Mean Pooling - Take attention mask into account for correct averaging
# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)
#
# # Load model from HuggingFace Hub
# tokenizer = AutoTokenizer.from_pretrained("D:\\01study\\text2vec-base")
# model = AutoModel.from_pretrained("D:\\01study\\text2vec-base")

# Tokenize sentences
# def simichnzn(sen1, sen2):
#     # Tokenize sentences
#     encoded_input = tokenizer([sen1, sen2], padding=True, truncation=True, return_tensors='pt')
#
#     # Compute token embeddings
#     with torch.no_grad():
#         model_output = model(**encoded_input)
#
#     # Perform pooling. In this case, mean pooling.
#     sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
#
#     normalized_vector1 = torch.nn.functional.normalize(sentence_embeddings[0].unsqueeze(0), dim=1)
#     normalized_vector2 = torch.nn.functional.normalize(sentence_embeddings[1].unsqueeze(0), dim=1)
#
#     # 计算余弦相似度
#     similarity = torch.nn.functional.cosine_similarity(normalized_vector1, normalized_vector2)
#
#     return similarity.item()
# SentenceModel("D:\\01study\\text2vec-base-multilingual")
#这个就是微调好的模型
sim_model = Similarity("D:\\01study\\text2vec-base-multilingual")


if __name__ == '__main__':
    name1 = get_mysql_list('earthdata', 'nasa1110', 'Entry_Title')
    name2 = get_mysql_list('earthdata', 'datatopic', 'DataName')
    # 合并两个列表
    combined_list = name2+ name1

    mainWord = get_mysql_list('earthdata', 'datatopic', 'MainWord')
    mainWord = [' '.join(inner_list) for inner_list in mainWord]
    term = get_mysql_list('earthdata', 'nasa1110', 'Term')
    variable_Level_1 = get_mysql_list('earthdata', 'nasa1110', 'Variable_Level_1')

    combined_data = [' '.join([item1[0], item2[0]]) for item1, item2 in zip(term, variable_Level_1)]
    mainWord.extend(combined_data)

    # 打印合并后的列表
    # print(combined_list)
    excel_name = "mixsimicon.xlsx"
    wb = openpyxl.load_workbook(excel_name)
    ws = wb.active

    # 获取当前选中的工作表

    sheet = wb.active
    column_names = ["name1", "name2", "关键词1", "关键词2", "内容关联度"]

    excel_name2 = "mixsimicon2.xlsx"
    wb2 = openpyxl.load_workbook(excel_name2)
    ws2 = wb2.active

    # 获取当前选中的工作表

    sheet2 = wb2.active
    column_names2 = ["name1", "name2", "关键词1", "关键词2", "内容关联度"]
    # 写入列名
    sheet2.append(column_names2)
    sheet.append(column_names)
    # sentence_embeddings=simichnzn(combined_list)
    for i in range(len(mainWord)):
        for j in  range(len(mainWord)):
            if i!=j:
                mixsimi=sim_model.get_scores(mainWord[i],mainWord[j])
                if len(mixsimi) > 0:
                    if mixsimi[0][0]>0.8:
                        data = [combined_list[i][0], combined_list[j][0], mainWord[i], mainWord[j], mixsimi[0][0]]
                        sheet2.append(data)
                    data1 = [combined_list[i][0], combined_list[j][0], mainWord[i], mainWord[j], mixsimi[0][0]]
                    sheet.append(data1)

    wb.save(excel_name)
    print('finish')
    wb2.save(excel_name2)
    print('finish')



    # print(sentence_embeddings)

