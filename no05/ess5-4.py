import py5

def setup():
   global angle
   py5.size(800, 400, py5.P3D)
   py5.no_stroke()
   angle = 0 # 角度を設定するための変数

def draw():
   global  angle
   py5.background(0)
   py5.directional_light(255,255,255, -1, 0, -1)
   py5.fill(0,104,183)
   py5.push_matrix()
   py5.translate(py5.width/2, py5.height/2) # 立体の中心を画面中央に移動
   py5.rotate_y(py5.radians(angle)) #Y軸に対してangleの数値分だけ回転
   py5.sphere(100)
   py5.pop_matrix()
   py5.translate(py5.width/2, py5.height/2)
   py5.fill(255)
   py5.push_matrix()
   py5.translate(150*py5.cos(py5.radians(angle)), 0, -150*py5.sin(py5.radians(angle)))
   py5.sphere(10)
   py5.pop_matrix()
   angle += 5

py5.run_sketch()
