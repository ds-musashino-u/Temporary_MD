import py5

def setup():
    global img
    py5.size(800,800)
    img = py5.load_image("../Image/cat.png")
def draw():
    py5.image(img, 0, 0)
py5.run_sketch()