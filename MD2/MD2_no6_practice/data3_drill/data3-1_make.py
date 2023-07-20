import pandas as pd
import numpy as np

# 広告ごとのクリック回数をランダムに生成します
np.random.seed(0)  # 一貫性のためのシード値
class_A_scores = np.round(np.random.normal(600, 400, 1000))  # Content_A 平均600、標準偏差10、人数100
class_B_scores = np.round(np.random.normal(750, 550, 1000))  # Content_B 平均750、標準偏差15、人数100
class_C_scores = np.round(np.random.normal(800, 400, 1000))  # Content_C 平均800、標準偏差20、人数100
class_D_scores = np.round(np.random.normal(450, 50, 1000))   # Content_D 平均450、標準偏差5、人数100

# データフレームを作成します
df = pd.DataFrame({
    'Content_A': class_A_scores,
    'Content_B': class_B_scores,
    'Content_C': class_C_scores,
    'Content_D': class_D_scores
})

# CSVファイルとして保存します
df.to_csv('data3.csv', index=False)
