from PIL import Image
import random

WIDTH = 616
HEIGHT = 400
INTENSITY = 0.001

####################

def matrix(x,y):
    return [(i//x,i%y) for i in range(x*y)]

class Sprite:
    def __init__(self,percent, data):
        self.percent = percent
        self.data = data

SPRITES = {
    "STAR_S": {
        "percent": 0.80,
        "data": [ # 1x1
            [1]
        ]
    },
    "STAR_M": {
        "percent": 0.10,
        "data": [ # 3x3
            [0,1,0],
            [1,1,1],
            [0,1,0]
        ]
    },
    "STAR_L": {
        "percent": 0.07,
        "data": [ # 13x13
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,1,0,0,1,0,0,1,0,0,0],
            [0,0,0,0,1,0,1,0,1,0,0,0,0],
            [0,0,0,0,0,1,1,1,0,0,0,0,0],
            [1,1,1,1,1,1,1,1,1,1,1,1,1],
            [0,0,0,0,0,1,1,1,0,0,0,0,0],
            [0,0,0,0,1,0,1,0,1,0,0,0,0],
            [0,0,0,1,0,0,1,0,0,1,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0,0,0,0,0,0]
        ]
    },
    "STAR_XL": {
        "percent": 0.03,
        "data": [ # 15x15
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
            [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
            [0,0,0,0,0,0,1,1,1,0,0,0,0,0,0],
            [0,0,0,0,0,1,0,1,0,1,0,0,0,0,0],
            [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
            [0,0,0,1,0,0,0,1,0,0,0,1,0,0,0],
            [0,0,1,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        ]
    },
}

SORTED_SPRITES = list(map(lambda s: Sprite(data=s.get("data"), percent=s.get("percent",0)), SPRITES.values()))
SORTED_SPRITES.sort(key=lambda s: s.percent)
assert sum([s.percent for s in SORTED_SPRITES]) == 1, "sum of percents must be equal to 1"

# Create a new blank image (black background by default)
# image = Image.new("RGB", (WIDTH, HEIGHT), "black")
image = Image.new("RGBA", (WIDTH, HEIGHT), "black")
pixels = image.load()

# Iterate through each pixel and set it to white based on COUNT
for x in range(WIDTH):
    for y in range(HEIGHT):
        rand = random.random()
        for s in SORTED_SPRITES:
            if rand < INTENSITY * s.percent:
                data_width = len(s.data)
                data_width_range = range(len(s.data))
                for i in data_width_range:
                    data_length = len(s.data[i])
                    data_length_range = range(len(s.data[i]))
                    for j in data_length_range:
                        ux = x+i-data_width//2
                        uy = y+j-data_length//2
                        if all(
                            [
                                s.data[i][j],
                                ux < WIDTH,
                                ux >= 0,
                                uy < HEIGHT,
                                uy >= 0
                            ]
                        ):
                            pixels[ux,uy] = (255,255,255)
                break

# Save the image
image.save("starrysky.png")
print("Image created and saved as 'starrysky.png'")
