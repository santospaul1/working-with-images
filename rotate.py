from PIL import Image

def main():
    try:
        img = Image.open("images/air.jpeg")
        # print(img)
        img = img.rotate(180);
        img.save("images/rotated_air.jpeg")
        
    except IOError:
        pass
if __name__ == "__main__":
    main()