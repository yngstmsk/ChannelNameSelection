#-*- coding: utf-8 -*-
import pandas as pd
from janome.tokenizer import Tokenizer
from Levenshtein import distance
import sys

# csvファイルを読み込み
df = pd.read_csv('/data/dic1.csv', header=None)

# 入力された名前
input_name = '圧ポンプHST吐出チャージ'

# 入力名の形態素解析
tokenizer = Tokenizer()
input_words = [token.surface for token in tokenizer.tokenize(input_name)]

# Levenshtein距離を用いて類似度を計算し、それぞれの行の名前の類似度を表示
similarities = {}
for i in range(len(df)):
    # 辞書ファイル登録名の形態素解析
    words = [token.surface for token in tokenizer.tokenize(df.iloc[i, 0])]
    
    # 並び替えてLevenshtein距離を計算
    sorted_input_words = sorted(input_words)
    sorted_words = sorted(words)
    similarity = distance(''.join(sorted_input_words), ''.join(sorted_words))
    
    similarities[df.iloc[i, 0]] = similarity

print('入力された名前:', input_name)

#Levebsgtain距離がどれくらい近いものまで出力するかを決めるmax_distanceを指定
max_distance = 5
similar_names = []
for name, similarity in similarities.items():
    print('"{0}"との類似度: {1}'.format(name, similarity))
    if similarity <= max_distance:
        similar_names.append(name)
print('入力された名前:', input_name)
print(similar_names)
