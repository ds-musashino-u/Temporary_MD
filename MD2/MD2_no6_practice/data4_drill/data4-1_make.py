import pandas as pd
import numpy as np

# 項目名
items = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']

# Q1のデータを2から4の範囲でランダムに生成（これにより分散が少し小さくなる）
Q1_data = np.random.randint(2, 5, size=(1000, 1))

# Q2のデータをランダムに生成
Q2_data = np.random.randint(1, 6, size=(1000, 1))

# Q3のデータを4か5で生成（これにより分散が小さくなる）
Q3_data = np.random.randint(4, 6, size=(1000, 1))

# Q2のデータにノイズを加えてQ5のデータを生成
noise = np.random.normal(0, 0.3, size=(1000, 1))
Q5_data = Q2_data + noise

# Q4のデータをランダムに生成
Q4_data = np.random.randint(1, 6, size=(1000, 1))

# Q5のデータが1から5の範囲外にならないようにクリップ
Q5_data = np.clip(Q5_data, 1, 5)

# Q5のデータを整数に丸める
Q5_data = np.rint(Q5_data).astype(int)

# 全てのデータを結合
data = np.concatenate([Q1_data, Q2_data, Q3_data, Q4_data, Q5_data], axis=1)

# DataFrameを作成
df = pd.DataFrame(data, columns=items)

# CSVファイルに保存
df.to_csv('data4.csv', index=False)
