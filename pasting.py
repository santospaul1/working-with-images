from PIL import Image

def main():
    try:
        img =Image.open("images/air.jpeg")
        img1 = Image.open("images/school.jpeg")
        img.paste(img1, (50, 50))

        img.save("images/pasted_air.jpeg")
    except IOError:
        pass
if __name__ == "__main__":
    main()