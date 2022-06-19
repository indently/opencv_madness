import cv2 as cv
from assets import assets
from helpers import image_helpers as och


def apply_threshold(thresholds: list[int], max_value: int, threshold_type):
    file = assets.numbers
    image = cv.imread(file, cv.IMREAD_GRAYSCALE)

    for threshold in thresholds:
        # Show numbers that meet the requirements for the min threshold amount
        thresh, output = cv.threshold(image, threshold, max_value, threshold_type)

        # Original image to compare
        # och.show_image('Original', image, time=1000)

        # Output image with specified Threshold
        och.show_image(f'Threshold: {threshold}', output, time=1000)


if __name__ == '__main__':
    # A range of thresholds for the greyscale value
    thresh_range = [0, 20, 100, 200, 240]

    # The max value for the intensity of the greyscale value
    max_thresh = 255

    # 1
    # Basic threshold

    # apply_threshold(thresholds=thresh_range,
    #                 max_value=max_thresh,
    #                 threshold_type=cv.THRESH_BINARY)

    # 2
    # Inverse threshold

    # apply_threshold(thresholds=thresh_range,
    #                 max_value=max_thresh,
    #                 threshold_type=cv.THRESH_BINARY_INV)

    # 3
    # Thresh trunc
    # Cuts everything below a certain limit
    # The threshold acts as a max limit, max_value is ignored

    # apply_threshold(thresholds=thresh_range,
    #                 max_value=max_thresh,
    #                 threshold_type=cv.THRESH_TRUNC)

    # 4
    # Thresh tozero
    # If the source pixels are more than the threshold, the destination gets set to the source, otherwise
    # destination is set to 0, max_value is ignored

    # Everything above the threshold remains the same, the rest get set to 0

    # apply_threshold(thresholds=thresh_range,
    #                 max_value=max_thresh,
    #                 threshold_type=cv.THRESH_TOZERO)

    # 5
    # Inverted thresh to zero

    # The inverse of thresh to zero, max_value is ignored

    # apply_threshold(thresholds=thresh_range,
    #                 max_value=max_thresh,
    #                 threshold_type=cv.THRESH_TOZERO_INV)




