import py5
import csv

def setup():
    py5.size(600,600)
    img_draw()
    draw_precipitation()
   
def draw_precipitation():
    with open('precipitation_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        py5.fill(0,0,255)
        for row in reader:
            x = float(row[1])
            y = float(row[2])
            precipitation = float(row[3])
            py5.rect(x,y, 10, -precipitation)

# def mouse_pressed():
#     if py5.mouse_button == py5.LEFT:
#         print(f"Mouse clicked at ({py5.mouse_x}, {py5.mouse_y})")
#         img_draw()
#         draw_precipitation()
#         py5.fill(0,0,0)
#         py5.text_font(py5.create_font("Arial", 16))
#         py5.text(f"Mouse clicked at ({py5.mouse_x}, {py5.mouse_y})",py5.width/2,py5.height)

def img_draw():
    img = py5.load_image("map.png")
    py5.image(img, 0,0,py5.width,py5.height)
        
py5.run_sketch()

py5.pri