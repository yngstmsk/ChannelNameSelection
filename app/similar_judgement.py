#-*- coding: utf-8 -*-
#辞書DBのリスト　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　
from multiprocessing.util import is_abstract_socket_namespace
import pandas as pd
import numpy as np
import itertools
import csv
from distutils.util import strtobool
from janome.tokenizer import Tokenizer

print(' ')
print('＊＊＊＊＊＊ここから＊＊＊＊＊＊?')
print(' ')
##辞書ファイルの読み込み
with open('dic_db.csv') as f:                                   #元pandatest_list.csv
    dic=f.read()
    print("1.csv辞書ファイル dic_db.csv= ",dic)                            #ブーム上げPPC圧力
    dic=dic.rsplit('\n')                                        #カンマ区切りのリストに変換
    list_dic_db=[]
    for i in dic:
        j=i.rsplit(',')
        list_dic_db.append(j)
    print("2.辞書ファイルlist_dic_db=",list_dic_db)
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
    
    
#**********ここからsimilar_judgement.pyオリジナル**********
#**********類似名判定**********
#同じ単語数の辞書ファイルを抽出
print("分割単語数=",len(learn_word_items))

#同じ単語のヒット数の高い順番に並べる


#違う単語で類似度の高い順番に並べる



    
#**********ここまでがsimilar_judgement.py**********
    
    

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

#　2.2　temp_ancer_list()で作成した論理演算結果文字列をlist型に変更し、1列目にチャンネル名に変更する
logical_word_list_str[0]=new_channel_name[0]                        #　1列目をタイトルに変換 ['アーム掘削PPC圧力','0','0','1','1']

#　3.list_dicにlogical_ancerを追加
list_dic_db.append(logical_word_list_str)                           #　listA,listB,list_ansを結合し、評価チャンネル名を既存の学習単語で判定した辞書リスト。list_dic=list_dic_db.append(logical_anser)としたらNoneになる。

#　4.add_dicの作成。辞書リストに評価リストのどの要素が同じか調べ、辞書リストに評価リストの解析結果行を追加する
#　4.1　nor_list_1の作成。辞書ファイルにない新しい要素を抜き出す。ここではアームと掘削
nor_list_1=list(set(learn_word_items) - set(same_word_list))
print('4.1nor_list_1=',nor_list_1)
#　4.2　nor_list_2の作成
list_dic_db_size=np.array(list_dic_db)                              #　辞書リストをnumpy配列(行列)にする。理由は下でzeros配列を作るのに配列サイズを数値化したいため。「3行5列」という解析結果が欲しい
nor_list_2=[]
if list_dic_db_size.shape[0]-2 > 1:
    for i in range(list_dic_db_size.shape[0]-2):
        nor_list_2.append([str(0)]*len(nor_list_1))
else:
    nor_list_2=[str(0)]*len(nor_list_1)  
print('4.2nor_list_2=',nor_list_2)
#　4.3　nor_list_3の作成  
nor_list_3=[str(1)]*len(nor_list_1)
print('4.3nor_list_3=',nor_list_3)
#　4.4　nor_list_1,2,3を結合しlist_add_dicを作成
def list_add_dic(nor_list_1,nor_list_2,nor_list_3):
    global list_add_dic
    list_list=[]
    list_list.append(nor_list_1)
    n=list_dic_db_size.shape[0]-2
    print('n=',n)
    if n > 1:                  
        for i in range(n):
            list_list.append(nor_list_2[i])
            list_add_dic=list_list
            #list_list=[list_list,nor_list_2[i]]
            print('4.4list_list=',list_list)
            #list_add_dic=list(itertools.chain.from_iterable(list_list)) #　リストの[]を外す
            #print('4.4.nor_list1,2=',list_add_dic)
    else:                                                            #　辞書ファイルが一つしかないからforループ不要
        list_add_dic=[list_list,nor_list_2]                          #　list2は1行なので、そのままlist_listに結合
        print('4.4nor_list1,2=',list_add_dic)
    list_add_dic.append(nor_list_3)                                  #　list_add_dicにlist_3を追加
list_add_dic(nor_list_1,nor_list_2,nor_list_3)
print('4.4list_add_dic=',list_add_dic)
#　5.作成したlist_add_dicをlist_dicに追加
for i in range(len(list_dic_db)):                                    #　リストの中の1つの配列ごとに後ろにlist_add_dicを追加する
    list_dic_db[i].extend(list_add_dic[i])                           #　求めたかった、もともとの辞書ファイルに評価チャンネル名とその評価結果、不足していた辞書単語を追加
print('5.list_dic_db=',list_dic_db)
    
    
    
#　6.追加結合リストの書き込み
#with open('pandastest_list.csv', 'w') as csv_file:                  #　r:読み取り,w:上書き,a:追加書き込み
#    writer=csv.writer(csv_file)                                     #　求めたかった、もともとの辞書ファイルに評価チャンネル名とその評価結果、不足していた辞書単語を追加
#    writer.writerows(list_dic_db)
#　7.評価リストの類似率を計算する。
#same_item_ratio=len(same_word_list)/(len(dic_word_items)-1)
