from PIL import Image
try:
    img = Image.open("images/air.jpeg")
    #print(img)
    width,height = img.size
except IOError:
    pass


img.save("images/air.jpeg")