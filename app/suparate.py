#-*- coding: utf-8 -*-
import csv

# csv�t�@�C����8��������
with open('std_log.txt', 'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    num_rows = 3329012
    chunk_size = num_rows // 4
    print(chunk_size)

    for i in range(8):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        if i == 7:
            end_idx = num_rows
        file_part = rows[start_idx:end_idx]
        print('i=', i)


        # �s�v�ȍs���폜���āA�V����csv�t�@�C���ɏ����o��
        with open(f'output_{i}.csv', 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            print('Done')
