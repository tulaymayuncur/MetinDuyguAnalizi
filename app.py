from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer, AutoModel
import torch.nn as nn
import heapq

app = Flask(__name__)

# Model ve tokenizer'ı yükle
tokenizer = AutoTokenizer.from_pretrained("maymuni/bert-base-turkish-cased-emotion-analysis")
bert = AutoModel.from_pretrained("maymuni/bert-base-turkish-cased-emotion-analysis", return_dict=False)

# Modelin parametrelerini dondur
for param in bert.parameters():
    param.requires_grad = False

class Arch(nn.Module):
    def __init__(self, bert):
        super(Arch, self).__init__()
        self.bert = bert 
        self.dropout = nn.Dropout(0.1)
        self.relu = nn.ReLU()
        self.fc1 = nn.Linear(768, 512)
        self.fc3 = nn.Linear(512, 9)
        self.softmax = nn.LogSoftmax(dim=1)
      
    def forward(self, sent_id, mask):
        _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)
        x = self.fc1(cls_hs)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc3(x)
        x = self.softmax(x)
        return x

device = torch.device('mps')

# Modeli tanımla ve yükle
model = Arch(bert)
model = model.to(device)
model.load_state_dict(torch.load('my_model_final.pt', map_location=device))

# Tahmin fonksiyonu
def predict_emotion(text):
    tokenized = tokenizer.encode_plus(
        text,
        pad_to_max_length=True,
        truncation=True,
        return_token_type_ids=False
    )

    input_ids = tokenized['input_ids']
    attention_mask = tokenized['attention_mask']

    seq = torch.tensor(input_ids).unsqueeze(0)
    mask = torch.tensor(attention_mask).unsqueeze(0)

    preds = model(seq.to(device), mask.to(device))
    preds = preds.detach().cpu().numpy()
    preds = torch.tensor(preds)
    probabilities = nn.functional.softmax(preds, dim=1)

    # En yüksek olasılıklı 3 duyguyu al
    top3_emotions = heapq.nlargest(3, enumerate(probabilities[0]), key=lambda x: x[1])

    # Duygu isimleri ve olasılıkları
    top3_emotion_names = ['kızgın', 'üzgün', 'korku', 'iğrenme', 'mutlu', 'aşk', 'merak', 'utanç', 'şaşkınlık']
    top3_emotion_probabilities = {top3_emotion_names[index]: float(prob) for index, prob in top3_emotions}

    return top3_emotion_probabilities

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_text = request.form['text']
        emotion_prediction = predict_emotion(user_text)
        return render_template('index.html', user_text=user_text, prediction=emotion_prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
