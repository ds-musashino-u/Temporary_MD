import py5

def setup():
    py5.size(600,400)
    py5.ellipse(py5.width/2, py5.height/2, 200,200)
    w = 100 * py5.cos(py5.radians(30))
    h = 100 * py5.sin(py5.radians(30))
    py5.ellipse(py5.width/2+w, py5.height/2-h, 100,100)

py5.run_sketch()

