#-*- coding: utf-8 -*-
#辞書DBのリスト　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
from multiprocessing.util import is_abstract_socket_namespace
import pandas as pd
import numpy as np
import itertools
import csv
from distutils.util import strtobool
from janome.tokenizer import Tokenizer
import copy

print(' ')
print('＊＊＊＊＊＊ここから＊＊＊＊＊＊?')
print(' ')
##辞書ファイルの読み込み
with open('dic_db.csv') as f:                                   #元pandatest_list.csv
    dic=f.read()
    print("1.csv辞書ファイル dic= ",dic)                         #ブーム,上げ,PPC,圧力,アーム,掘削 ブーム上げPPC圧力,1,1,1,1,0,0 アーム掘削PPC圧力,0,0,1,1,1,1
    dic=dic.rsplit('\n')                                        #カンマ区切りのリストに変換
    list_dic_db=[]
    for i in dic:                   #[['0', 'ブーム', '上げ', 'PPC', '圧力', 'アーム', '掘削'], ['ブーム上げPPC圧力', '1', '1', '1', '1', '0', '0'], ['アーム掘削PPC圧力', '0', '0', '1', '1', '1', '1']]
        j=i.rsplit(',')
        list_dic_db.append(j)
    print("2.辞書ファイルlist_dic_db=",list_dic_db)     
#**********ここからsimilar_judgement.pyオリジナル**********
#辞書ファイルのサイズ(n*m)を取得する
#print('dic行サイズ=',len(list_dic_db))     #行数   今の場合は3
#print('dic列サイズ=',len(list_dic_db[0]))  #列数　 今の場合は7

#指定列の合計を算出する
#辞書ファイルの1行目と1列目を削除し、各行の合計を求め、sum_listリストに追加する
list_dic_db2=[]         #apendやdelすると元リストもコピーリストも変わってしまうので、元リストをコピーリストと切り離す　https://qiita.com/kokorinosoba/items/e9ab9398af5b44d2ac9a
list_dic_db2.append(copy.deepcopy(list_dic_db)) 
list_dic_db2=list_dic_db2[0]        #リスト多重化しているので、ひとつ[]を消して元に戻す
del(list_dic_db2[0])                         #list_dic_dbの1行目の単語リストを削除 [['ブーム上げPPC圧力', '1', '1', '1', '1', '0', '0'], ['アーム掘削PPC圧力', '0', '0', '1', '1', '1', '1']]
print("list_dic_db2=",list_dic_db2)

dic_size_Row=len(list_dic_db2)               #行数   今の場合は2
print("dic_size_Row=",dic_size_Row)

print("ここからfor文")

sum_list=[0]
for n in range(len(list_dic_db2)):
    print("n=",n)
    dic1=list_dic_db2[n]
    del dic1[0]                                 #1列目のチャンネル名を削除し、数字のみのリストにする['1', '1', '1', '1', '0', '0']
    print("dic_title=",dic1)
    dic1_int=[int(n) for n in dic1]             #全体合計できるようにstr型なのでint型に変換する [1, 1, 1, 1, 0, 0]
    print("dic1_int=2",dic1_int)
    sum_value=sum(dic1_int)                     #全体合計する　ここでは4
    print("sum=",sum_value)
    #合計リストに追加する
    sum_list.append(sum_value)
print("sum_list=",sum_list)                     #[0,4,4]という形のリストが作成できた

#sum_listと評価ファイルの単語数と同じ単語数のチャンネル名を摘出する。

#評価ファイルの読み込み
with open('test2.csv',encoding="Shift-JIS") as f:
    new_channel_name=f.read()
    print("3.3.評価file *****.csv=",new_channel_name)            #ブーム上げPPC圧力
    new_channel_name=new_channel_name.rsplit(',')                #カンマ区切りのリストに変換
    new_channel_name=list(map(lambda new_channel_name:new_channel_name.rstrip("\n"),new_channel_name))      #改行削除
t = Tokenizer()
learn_word_items = []                                           #アウトプット１：チャンネル名の分割化リスト:learn_word_items
for item in new_channel_name:
    for token in t.tokenize(item):
        l=token.surface
        learn_word_items.append(l)
    print("評価ファイルリスト化learn_word_items=",learn_word_items)     #ここで評価チャンネル名分割完了    
print("分割単語数=",len(learn_word_items))

dic_word_items=list_dic_db[0]                                       #辞書ファイルに登録されている要素を取り出す['0','ブーム','上げ','PPC','圧力'] 

#辞書ファイルと同じ要素の列を1、違うものを0とするlist_ansを作成
same_word_list = list(set(dic_word_items) & set(learn_word_items))  #同じ要素を取得する
print('2.same_word_list=',same_word_list)
print('2.dic_word_items=',dic_word_items)
#　2.1　辞書ファイルに登録されている要素が評価ファイルの中にあれば1、なければ0のリストを作成する
def temp_anser_list():
    global logical_word_list_str
    logical_lists=[]                                                #logical_dataの要素を持ったlistの作成
    #add_listがlistAの何番目に入っているかを調べ、入っていない列は0、入っている列を1にするリストを作成する
    for i in same_word_list:                                        #重複する要素リストsame_items_list[PPC,圧力]のi番目を抜き出す　
        logical_lists.append(list([i == j for j in dic_word_items] ))            #same_listの一つの要素が何番目に入っているかわかったら空のlistCに追加し、複数の要素をリスト化する
    logical_items_int=logical_lists[0]                              #logical_listsの1つ目の要素をlogocal_items_intとする [[0,0,0,1,0][0,0,0,0,1]
    #add_listの全ての要素のorを取ってひとまとめのリストを作成する
    logical_list_bool=[]
    for x in range(len(logical_lists)):                             #cの要素の数だけ、np.logical_orをし続ける。
        logical_list_bool = [num1 or num2 for num1, num2 in zip(logical_lists[x],logical_items_int)]
    logical_list_int=[int(n) for n in logical_list_bool]            #bool型リストをint型に変換 [0, 0, 0, 1, 1]
    print('2.1.logical_list_int=',logical_list_int)
    logical_word_list_str=[str(n) for n in logical_list_int]        #int型のリストをstr型に変換 ['0','0','0','1','1']
    print('2.1.logical_word_list_str=',logical_word_list_str)
temp_anser_list()

sorted_dic_list=[]
#同じ単語数の辞書ファイルを抽出
for n in range(len(list_dic_db)):
    if len(learn_word_items) == sum_list[n]:
        sorted_dic_list.append(list_dic_db[n])
print("sorted_dic_list=",sorted_dic_list)

#logical_list_intは評価ファイルの単語が辞書ファイルのどこと同じか分析した結果。このリストとsorted_dic_listの各要素といくつ同じものがあるかをカウントして順番に並べる。
#つまり、同じ単語のヒット数の高い順番に並べる




#違う単語で類似度の高い順番に並べる



    