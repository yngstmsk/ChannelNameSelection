#-*- coding: utf-8
import pandas as pd
import Levenshtein

# csvファイルを読み込み
df = pd.read_csv('dic.csv', header=None)

# 入力された名前
input_name = '上PPC圧ブーム'

# Levenshtein距離を用いて類似度を計算し、それぞれの行の名前の類似度を表示
similarities = {}
for i in range(len(df)):
    similarity = Levenshtein.distance(input_name, df.iloc[i, 0])
    similarities[df.iloc[i, 0]] = similarity

# 結果を表示
print('入力された名前:', input_name)
for name, similarity in similarities.items():
    print('"{0}"との類似度: {1}'.format(name, similarity))

