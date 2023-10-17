from PIL import Image

def main():
    try:
        img = Image.open("images/air.jpeg")
        jax = img.split()
        print(img.split())
    except IOError:
        pass

if __name__ == "__main__":
    main()
