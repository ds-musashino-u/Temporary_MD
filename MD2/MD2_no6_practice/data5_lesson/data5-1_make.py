import pandas as pd
import numpy as np
import random
import string

# ランダムな名前を生成するための関数
def random_name(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# 20人の名前を生成
names = [random_name(5) for _ in range(200)]

# 数学、英語、国語の得点をランダムに生成
math_scores = np.random.randint(50, 100, size=200)
english_scores = np.random.randint(50, 100, size=200)
japanese_scores = np.random.randint(50, 100, size=200)

# データフレームを作成
df = pd.DataFrame({
    'Name': names,
    'Math': math_scores,
    'English': english_scores,
    'Japanese': japanese_scores
})

# CSVファイルとして出力
df.to_csv('data5.csv', index=False)
