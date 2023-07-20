import pandas as pd
import numpy as np

# np.random.randintを使用して200人分の数学と英語の得点を生成
# ここでは数学を20から70の範囲でランダムに生成、英語を0から100の範囲でランダムに生成
# 数学のデータのバラツキを意図的に小さく設定
math_scores = np.random.randint(20, 71, 200)
english_scores = np.random.randint(0, 101, 200)

# pandasのDataFrameを作成
df = pd.DataFrame({
    'Math': math_scores,
    'English': english_scores
})

# CSVファイルとして保存
df.to_csv('data1.csv', index=False)