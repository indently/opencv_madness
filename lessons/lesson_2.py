import cv2 as cv
from assets import assets
import numpy as np
import sys


def play_video(file: str, webcam: bool = False):
    if webcam:
        # If you get an error you need to make sure you either have a WEBCAM
        # or that you have webcam permissions enabled for PyCharm
        video = cv.VideoCapture(0)
    else:
        # Open any video file
        video = cv.VideoCapture(file)

    if not video.isOpened():
        print('Error opening the video file')
    else:
        fps = video.get(cv.CAP_PROP_FPS)
        frame_count = video.get(cv.CAP_PROP_FRAME_COUNT)
        width, height = int(video.get(cv.CAP_PROP_FRAME_WIDTH)), int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
        frame_size = (width, height)

        print('Video details:')
        print('FPS:', round(fps, 2))
        print('Frame count:', frame_count)
        print(f'H {height}, W {width}')

        # There are many formats, you will have to search these on Google
        codec = cv.VideoWriter_fourcc(*'mp4v')
        output = cv.VideoWriter('output.mp4', codec, fps, frame_size)

        while video.isOpened():
            success, frame = video.read()
            # If there is a frame to show
            if success:
                cv.imshow('Frame', frame)
                output.write(frame)
                cv.waitKey(10)
            else:
                print('Stream finished...')
                break

    video.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    play_video(file=assets.birds, webcam=False)
