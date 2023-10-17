from PIL import Image

def main():
    try:
        img = Image.open("images/air.jpeg")

        print(img.histogram())
    except:
        pass
if __name__ == "__main__":
    main()