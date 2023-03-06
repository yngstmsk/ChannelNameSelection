import csv

# csvファイルを読み込み
with open('std_log.txt', 'r') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

# 不要な行を削除
rows = [row for row in rows if not '= ****' in row]

# 新しいcsvファイルを書き出し
with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)
