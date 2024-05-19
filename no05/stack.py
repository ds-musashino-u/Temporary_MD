stack = []

# プッシュ操作
stack.append(1)
stack.append(2)
stack.append(3)

print("スタック:", stack)  # 出力: スタック: [1, 2, 3]

# ポップ操作
top = stack.pop()
print("取り出したデータ:", top)  # 出力: 取り出したデータ: 3
print("スタック:", stack)  # 出力: スタック: [1, 2]
