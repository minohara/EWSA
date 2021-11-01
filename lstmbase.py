# coding: utf-8
import sys
import csv
# sys.path.append('..')
sys.path.append(r'C:\Users\ipodv\Deep learning\atom pythoncode')
from common.optimizer import SGD
from common.trainer import RnnlmTrainer
from common.util import eval_perplexity
#from dataset import ptb
from rnnlm01 import Rnnlm


# ハイパーパラメータの設定
batch_size = 20
wordvec_size = 100
hidden_size = 100  # RNNの隠れ状態ベクトルの要素数
time_size = 35  # RNNを展開するサイズ
lr = 20.0
max_epoch = 100
max_grad = 0.25

# センサーデータ(CSV)から，カラムを指定してデータを読み込む
data = list()
with open("fp01.csv") as csvfile:
    rawData = csv.reader(csvfile, delimiter=",")
    i = -1 # 先頭のデータを飛ばす
    for row in rawData:
        if (i % 4) == 0: # 4つごとに使う
            data.append(float(row[4])) # カラム 4 のデータを使う
        i = i + 1

print(i)

# 学習データの読み込み
# corpus, word_to_id, id_to_word = ptb.load_data('train')
# data = ptb.load_data('train')
# corpus_test, _, _ = ptb.load_data('test')
# data_test, _, _ = ptb.load_data('test')
# vocab_size = len(word_to_id)
learnSize = 2000

xs = data[:learnSize-1]
ts = data[1:learnSize]

data_test = data[learnSize+1:]

# モデルの生成
model = Rnnlm(wordvec_size, hidden_size)
optimizer = SGD(lr)
trainer = RnnlmTrainer(model, optimizer)

# 勾配クリッピングを適用して学習
trainer.fit(xs, ts, max_epoch, batch_size, time_size, max_grad,
            eval_interval=20)
trainer.plot(ylim=(0, 100))

# テストデータで評価
model.reset_state()
# ppl_test = eval_perplexity(model, corpus_test)
ppl_test = eval_perplexity(model, data)
print('test perplexity: ', ppl_test)

# パラメータの保存
model.save_params()
