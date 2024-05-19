import py5
import csv

def setup():
    py5.size(600,600)
    py5.fill(0,0,255)
    img = py5.load_image("map.png")
    py5.image(img, 0,0,py5.width,py5.height)
    draw_precipitation()

def draw_precipitation():
    with open('precipitation_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            x = int(row[1])
            y = int(row[2])
            precipitation = float(row[3])
            py5.rect(x,y, 10, -precipitation)

py5.run_sketch()