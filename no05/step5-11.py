import py5

def setup():
    global angle
    py5.size(400, 400,py5.P3D)
    py5.background(0)
    
    angle = 0
    
def draw():
    global angle
    py5.background(0)
    py5.directional_light(0,255,0,0,0.5,-1)
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_x(py5.radians(-30))
    py5.rotate_y(py5.radians(angle))
    py5.box(150)
    angle += 10
        
py5.run_sketch()
