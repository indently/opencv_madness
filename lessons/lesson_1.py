import cv2 as cv
from assets import assets
import sys


def main():
    # Our local file
    file = assets.cat_image

    # Reads an image file
    image = cv.imread(file, cv.IMREAD_COLOR)  # cv.IMREAD_GRAYSCALE for greyscale

    # Exits the program if the image cannot be read
    if image is None:
        sys.exit("Could not read the image.")

    # Shows the image
    cv.imshow('Image', image)

    # Waits for any keystroke with a 3000-millisecond delay; insert 0 for infinite
    key = cv.waitKey(3000)

    # If user taps: 's'
    # Saves th processed image (Writes it in a directory)
    if key == ord("s"):
        cv.imwrite('output.png', image)

    cv.destroyAllWindows()
    sys.exit("Finished!")


if __name__ == '__main__':
    main()
