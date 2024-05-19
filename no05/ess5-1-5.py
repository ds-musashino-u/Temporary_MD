import py5

def setup():
    py5.size(600,400)
    py5.ellipse(py5.width/2, py5.height/2, 200,200)
    
    for i in range(0,360,30):
        py5.ellipse(py5.width/2 + calcu_W(100,i), py5.height/2 - calcu_H(100,i), 100,100)

def calcu_W(W, angle):
    return W * py5.cos(py5.radians(angle))

def calcu_H(H, angle):
    return H * py5.sin(py5.radians(angle))

py5.run_sketch()

