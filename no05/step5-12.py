import py5
def setup():
  py5.size(800, 400, py5.P3D)
  py5.no_stroke()
  py5.background(0)
  py5.directional_light(255,255,255, -1, 0, -1)
  py5.fill(0,104,183)
  py5.push_matrix()
  py5.translate(py5.width/2, py5.height/2) 
  py5.sphere(100)
  py5.pop_matrix()
  py5.translate(py5.width/2, py5.height/2)
  py5.fill(255)
  py5.translate(116, 0, 95)
  py5.sphere(10)
py5.run_sketch()