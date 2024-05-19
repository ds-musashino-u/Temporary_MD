

def calculate_trapezoid_area(base1, base2, height):
    """
    台形の底辺1、底辺2、高さを与えられた場合に、台形の面積を計算します。
    """
    return (base1 + base2) * height / 2

# 例の使用方法
base1 = 5
base2 = 7
height = 3
area = calculate_trapezoid_area(base1, base2, height)
print("台形の面積は:", area)

