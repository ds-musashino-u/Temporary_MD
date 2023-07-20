import pandas as pd
import numpy as np

# np.random.randintを使用して400人分の日本語の得点を生成
# ここでは日本語を0から100の範囲でランダムに生成
japanese_scores = np.random.randint(0, 101, 400)

# 理科のスコアは日本語のスコアに基づいて生成する
# ここでは日本語のスコアの一部と一部のランダムなノイズを組み合わせています
# np.clipを用いて、スコアが0未満または100を超えないようにしています
noise = np.random.normal(0, 10, 400) # 平均0、標準偏差10のノイズ
science_scores = np.clip(japanese_scores / 2 + noise, 0, 100) # 日本語のスコアの半分にノイズを加える

# 理科のスコアを整数に丸める
science_scores = np.round(science_scores).astype(int)

# pandasのDataFrameを作成
df = pd.DataFrame({
    'Japanese': japanese_scores,
    'Science': science_scores
})

# CSVファイルとして保存
df.to_csv('data2.csv', index=False)
