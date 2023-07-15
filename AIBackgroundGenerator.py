import cv2
import webcolors
from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys
from rembg import remove
from PIL import Image
import os
import openai 

print(os.getcwd())

openai.api_key = "             "

cam = cv2.VideoCapture(0)
cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break

    cv2.imshow("Python Webcam Screenshot App", frame)

    k = cv2.waitKey(1)  

    if k % 256 == 27:  # Escape key  
        print("Escape hit, closing the app")
        break
    elif k % 256 == 32:  # Space key
        img_name = "input{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("screenshot taken")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()

img = Image.open("input0.png")
R = remove(img)
R.save("output1.png")

ct = ColorThief("output1.png")
dominant_color = ct.get_color(quality=1)

plt.imshow([[dominant_color]])
plt.show()

palette = ct.get_palette(color_count=5)
plt.imshow([[palette[i] for i in range(5)]])
plt.show()

og1 = palette[0]
og2 = palette[1]
og3 = palette[2]
og4 = palette[3]
og5 = palette[4]

def calculate_complementary_color(rgb_color):
    complementary_color = tuple(255 - value for value in rgb_color)
    return complementary_color

og1 = og1
og2 = og2
og3 = og3
og4 = og4
og5 = og5

color1 = calculate_complementary_color(og1)
color2 = calculate_complementary_color(og2)
color3 = calculate_complementary_color(og3)
color4 = calculate_complementary_color(og4)
color5 = calculate_complementary_color(og5)
domcomplement = calculate_complementary_color(dominant_color)

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                         (g - rgb[1]) ** 2,
                         (b - rgb[2]) ** 2])] = color_name
    return differences[min(differences.keys())]

color1 = color1
color2 = color2
color3 = color3
color4 = color4
color5 = color5

try:
    name_og1 = webcolors.rgb_to_name(og1)
    
except ValueError:
    name_og1 = closest_color(og1)
    
plt.imshow([[og1]])
plt.show()

try:
    name_og2 = webcolors.rgb_to_name(og2)
    
except ValueError:
    name_og2 = closest_color(og2)
    
plt.imshow([[og2]])
plt.show()

try: 
    cname1 = webcolors.rgb_to_name(color1)
    #print(f"The color is exactly {cname1}")
except ValueError:
    cname1 = closest_color(color1)
    #print(f"The color is closest to {cname1}")    

#plt.imshow([[color1]])     
#plt.show()     
    
try: 
    cname2 = webcolors.rgb_to_name(color2)
    #print(f"The color is exactly {cname2}")
except ValueError:
    cname2 = closest_color(color2)
    #print(f"The color is closest to {cname2}")  

#plt.imshow([[color2]])     
#plt.show()

try:
    cname_dom = webcolors.rgb_to_name(dominant_color)

except ValueError:
    cname_dom = closest_color(dominant_color)
                                      
try: 
    cname3 = webcolors.rgb_to_name(color3)
    #print(f"The color is exactly {cname3}")
except ValueError:
    cname3 = closest_color(color3)
    #print(f"The color is closest to {cname3}")  

#plt.imshow([[color3]])     
#plt.show()

try: 
    cname4 = webcolors.rgb_to_name(color4)
    #print(f"The color is exactly {cname4}")
except ValueError:
    cname4 = closest_color(color4)
    #print(f"The color is closest to {cname4}")  

#plt.imshow([[color4]])     
#plt.show()

try: 
    cname5 = webcolors.rgb_to_name(color5)
    #print(f"The color is exactly {cname5}")
except ValueError:
    cname5 = closest_color(color5)
    #print(f"The color is closest to {cname5}")  
    
try:
    domname = webcolors.rgb_to_name(domcomplement)
    #print(f"The color is exactly {domname}")
except ValueError:
    domname = closest_color(domcomplement)
    #print(f"the color is exactly {domname}")

#plt.imshow([[color5]])     
#plt.show()



def convert_to_analogous(rgb):
    hls = colorsys.rgb_to_hls(rgb[0] / 255, rgb[1] / 255, rgb[2] / 255)
    hls1 = ((hls[0] + 1 / 12) % 1, hls[1], hls[2])  
    hls2 = ((hls[0] - 1 / 12) % 1, hls[1], hls[2])  
    rgb1 = colorsys.hls_to_rgb(hls1[0], hls1[1], hls1[2])
    rgb2 = colorsys.hls_to_rgb(hls2[0], hls2[1], hls2[2])
    return tuple(int(x * 255) for x in rgb1), tuple(int(x * 255) for x in rgb2)

analogous_color1, analogous_color2 = convert_to_analogous(dominant_color)

try:
    cname_analogous1 = webcolors.rgb_to_name(analogous_color1)
    #print(f"The first analogous color is exactly {cname_analogous1}")
except ValueError:
    cname_analogous1 = closest_color(analogous_color1)
    #print(f"The first analogous color is closest to {cname_analogous1}")

#plt.imshow([[analogous_color1]])
#plt.show()

try:
    cname_analogous2 = webcolors.rgb_to_name(analogous_color2)
    #print(f"The second analogous color is exactly {cname_analogous2}")
except ValueError:
    cname_analogous2 = closest_color(analogous_color2)
    #print(f"The second analogous color is closest to {cname_analogous2}")

#plt.imshow([[analogous_color2]])
#plt.show()


print(f"The analogous are {name_og1}, {name_og2}.")


print(f"A minimalist artistic design with the following colors: {cname1}, {cname2}, {cname3}, {cname4}, {cname5}.") 

promptinput_analogous = f'a realistic photo of a living room with the following colors: {cname_analogous1} and {cname_analogous2}.' 

res_analogous = openai.Image.create(
prompt = promptinput_analogous,
n = 1,
size = "512x512",
)

promptinput_complementary = f'a realistic photo of a living room with the following colors: {cname1} and {cname2}'

res_complementary = openai.Image.create(
    prompt = promptinput_complementary,
    n=1,
    size="512x512",
)

promptinput_og = f'a realistic photo of a living room with the following colors: {og1} and {og2}.'

res_og = openai.Image.create(
    prompt = promptinput_og,
    n=1,
    size="512x512",
)

print(f'analogous: {res_analogous}')
print(f'complementary: {res_complementary}')
print(f'og:{res_og}')