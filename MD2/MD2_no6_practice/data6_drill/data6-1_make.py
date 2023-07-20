import pandas as pd
import numpy as np

# ユーザー名
users = ['User' + str(i) for i in range(1, 201)]

# 各コンテンツごとにデータを生成
VideoA = np.random.randint(0, 101, 200)
VideoB = np.round(np.random.normal(50, 30, 200)).clip(0, 100)  # 平均50、標準偏差30で生成し、0～100の範囲にクリップして整数に丸める
VideoC = np.random.randint(0, 101, 200)
VideoD = np.round(np.random.normal(50, 5, 200)).clip(0, 100)  # 平均50、標準偏差5で生成し、0～100の範囲にクリップして整数に丸める
VideoE = np.random.randint(0, 101, 200)
# 同様に追加のコンテンツデータを生成
VideoF = np.random.randint(0, 101, 200)
VideoG = np.round(np.random.normal(50, 20, 200)).clip(0, 100)
VideoH = np.random.randint(0, 101, 200)
VideoI = np.round(np.random.normal(50, 10, 200)).clip(0, 100)
VideoJ = np.random.randint(0, 101, 200)

# DataFrameを作成
df = pd.DataFrame({
    'Name': users,
    'VideoA': VideoA,
    'VideoB': VideoB,
    'VideoC': VideoC,
    'VideoD': VideoD,
    'VideoE': VideoE,
    'VideoF': VideoF,
    'VideoG': VideoG,
    'VideoH': VideoH,
    'VideoI': VideoI,
    'VideoJ': VideoJ
})

# CSVファイルに保存
df.to_csv('data6.csv',index=False)
