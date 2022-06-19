import cv2 as cv


# Shows the image at the given coordinate on top focus for 2 seconds
def show_image(window_name, image, time=0):
    cv.imshow(window_name, image)
    cv.setWindowProperty(window_name, cv.WND_PROP_TOPMOST, 1)
    cv.moveWindow(window_name, 100, 100)
    cv.waitKey(time)
