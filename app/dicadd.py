#-*- coding:  Shift-JIS -*-
import csv
from janome.tokenizer import Tokenizer

new_channel_name = "�u�[����PPC��"

# �����t�@�C���̓ǂݍ���
with open('dic1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    dictionary = list(reader)

# �`�ԑf��͂��ĒP����擾����֐�
def tokenize(channel_name):
    t = Tokenizer()
    tokens = t.tokenize(channel_name)
    # �����������o��
    words = [token.surface for token in tokens if token.part_of_speech.split(',')[0] == '����']
    return words

# �V�����P����擾����
new_words = tokenize(new_channel_name)

# �V�����P�ꂪ�����ɑ��݂��Ȃ��ꍇ�͐V�������ǉ�����
for word in new_words:
    if word not in dictionary[0]:
        dictionary[0].append(word)
        for i in range(1, len(dictionary)):
            dictionary[i].append("0")

# �V�����`�����l�����������ɒǉ�����
new_row = [new_channel_name]
for i in range(1, len(dictionary[0])):
    if dictionary[0][i] in new_words:
        new_row.append("1")
    else:
        new_row.append("0")

dictionary.append(new_row)

# �������t�@�C���ɏo�͂���
with open('dic.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dictionary)
