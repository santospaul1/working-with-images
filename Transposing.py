from PIL import Image

def main():
    try:
        img = open("images/air.jpeg")
        transpose = img.transpose(Image.FLIP_LEFT_RIGHT)
        transpose.save("images/transposed.jpeg")


    except IOError:
        pass
if __name__ =="__main__":
    main()