import csv

# センサーデータ(CSV)から，カラムを指定してデータを読み込む
data = list()
with open("fp01.csv") as csvfile:
    rawData = csv.reader(csvfile, delimiter=",")
    i = 0
    for row in rawData:
        if (i % 4) == 0: # 4つごとに使う
            data.append(row[4]) # カラム 4 のデータを使う
        i = i + 1
print(data)
