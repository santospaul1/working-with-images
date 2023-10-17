from PIL import Image

def main():
    try:
        img = Image.open("images/air.jpeg")
        width, height = img.size
        area = (0,0,width/2,height/2)
        img = img.crop(area)
        img.save("images/cropped_air.png")
    except IOError:
        pass
if __name__ == "__main__":
    main()


