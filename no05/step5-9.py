import py5

def setup():
    py5.size(400, 400,py5.P3D)
    py5.background(0)
    py5.ambient_light(255, 100, 100)
    py5.translate(py5.width / 2, py5.height / 2, 0)
    py5.rotate_x(py5.radians(-30))
    py5.rotate_y(py5.radians(30))
    py5.box(150)
        
py5.run_sketch()
