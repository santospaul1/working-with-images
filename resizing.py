from PIL import Image


def main():
    try:
        # Relative Path
        img = Image.open("images/air.jpeg")
        width, height = img.size

        img = img.resize((width/2, height/2))

        # Saved in the same relative location
        img.save("images/resized_picture.jpg")
    except IOError:
        print("image not found")


if __name__ == "__main__":
    main()