#-*- coding:  Shift-JIS -*-
import csv
from janome.tokenizer import Tokenizer

new_channel_name = "ブーム上PPC圧"

# 辞書ファイルの読み込み
with open('dic1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    dictionary = list(reader)

# 形態素解析して単語を取得する関数
def tokenize(channel_name):
    t = Tokenizer()
    tokens = t.tokenize(channel_name)
    # 名詞だけ取り出す
    words = [token.surface for token in tokens if token.part_of_speech.split(',')[0] == '名詞']
    return words

# 新しい単語を取得する
new_words = tokenize(new_channel_name)

# 新しい単語が辞書に存在しない場合は新しい列を追加する
for word in new_words:
    if word not in dictionary[0]:
        dictionary[0].append(word)
        for i in range(1, len(dictionary)):
            dictionary[i].append("0")

# 新しいチャンネル名を辞書に追加する
new_row = [new_channel_name]
for i in range(1, len(dictionary[0])):
    if dictionary[0][i] in new_words:
        new_row.append("1")
    else:
        new_row.append("0")

dictionary.append(new_row)

# 辞書をファイルに出力する
with open('dic.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dictionary)
