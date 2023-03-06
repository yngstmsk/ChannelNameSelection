#-*- coding: utf-8 -*-
import csv

# csv�t�@�C����8��������
with open('std_log.txt', 'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    num_rows = len(rows)
    chunk_size = num_rows // 8
    for i in range(8):
        start_idx = i * chunk_size
        end_idx = start_idx + chunk_size
        if i == 7:
            end_idx = num_rows
        file_part = rows[start_idx:end_idx]

        # �s�v�ȍs���폜���āA�V����csv�t�@�C���ɏ����o��
        with open(f'output_{i}.csv', 'w', newline='') as f_out:
            writer = csv.writer(f_out)
            for row in file_part:
                if not '= ***** ' in row:
                    writer.writerow(row)

# 8�̃t�@�C������������
combined_rows = []
for i in range(8):
    with open(f'output_{i}.csv', 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        combined_rows += rows

# �V����csv�t�@�C���������o��
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(combined_rows)
