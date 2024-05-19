import py5

def setup():
    py5.size(400, 400,py5.P3D)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.box(100)
    
py5.run_sketch()
