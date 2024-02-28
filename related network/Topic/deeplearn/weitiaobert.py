import json
import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertModel, AdamW

# 自定义数据集类
class KeywordSimilarityDataset(Dataset):
    def __init__(self, data, tokenizer):
        self.tokenizer = tokenizer
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        text1, text2, label = self.data[idx]
        encoded = self.tokenizer.encode_plus(
            text1,
            text2,
            add_special_tokens=True,
            max_length=256,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )
        input_ids = encoded['input_ids'].squeeze()
        attention_mask = encoded['attention_mask'].squeeze()
        label = torch.tensor(label).float()

        return input_ids, attention_mask, label


# 模型定义
class KeywordSimilarityModel(nn.Module):
    def __init__(self, num_classes):
        super(KeywordSimilarityModel, self).__init__()
        self.bert = BertModel.from_pretrained('D:\\01study\\text2vec-base-multilingual',do_lower_case=True)
        self.dropout = nn.Dropout(0.1)
        self.fc = nn.Linear(768, num_classes)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.pooler_output
        pooled_output = self.dropout(pooled_output)
        logits = self.fc(pooled_output)
        return logits


# 数据准备
tokenizer = BertTokenizer.from_pretrained('D:\\01study\\text2vec-base-multilingual')
file_path = 'newall.jsonl'

with open(file_path, 'r') as file:
    lines = file.readlines()

data = []
for line in lines:
    json_obj = json.loads(line)
    text1 = json_obj['text1']
    text2 = json_obj['text2']
    label = json_obj['label']
    data.append((text1, text2, label))

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

train_dataset = KeywordSimilarityDataset(train_data, tokenizer)
test_dataset = KeywordSimilarityDataset(test_data, tokenizer)

train_dataloader = DataLoader(train_dataset, batch_size=16, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=16, shuffle=False)

# 模型和优化器
model = KeywordSimilarityModel(num_classes=1)
optimizer = AdamW(model.parameters(), lr=2e-5)

# 训练和评估
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

num_epochs = 5
total_steps = len(train_dataloader) * num_epochs
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=1, gamma=0.1)

for epoch in range(num_epochs):
    model.train()
    total_loss = 0

    for batch in train_dataloader:
        input_ids, attention_mask, labels = batch
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        logits = model(input_ids, attention_mask)
        loss_fn = nn.MSELoss()
        loss = loss_fn(logits.squeeze(), labels)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_dataloader)
    print(f"Epoch {epoch+1} - Average training loss: {avg_loss}")

    model.eval()
    with torch.no_grad():
        total_loss = 0
        for batch in test_dataloader:
            input_ids, attention_mask, labels = batch
            input_ids = input_ids.to(device)
            attention_mask = attention_mask.to(device)
            labels = labels.to(device)

            logits = model(input_ids, attention_mask)
            loss_fn = nn.MSELoss()
            loss = loss_fn(logits.squeeze(), labels)

            total_loss += loss.item()

        avg_loss = total_loss / len(test_dataloader)
        print(f"Epoch {epoch+1} - Average validation loss: {avg_loss}")

    scheduler.step()

# 保存模型
torch.save(model.state_dict(), 'modelweitiao')


# # 加载模型
# model = KeywordSimilarityModel(num_classes=1)
# model.load_state_dict(torch.load('model.pth'))