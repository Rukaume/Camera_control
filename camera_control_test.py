import cv2
import numpy as np
import time
import matplotlib.pyplot as plt

# parameters
time_interval = 0.3  # (sec)
images = 100  # Number of images
window_size = (480, 640)
pixel_threshold = 0.5


def Image_subtraction(time_interval, images):
    # current time
    init_image = np.zeros(window_size)
    result_data = []
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, window_size[1])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, window_size[0])
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    for i in range(images):
        if i == 0:
            _, image = cap.read()
            image = cv2.cvtColor(image,
                                 cv2.COLOR_BGR2GRAY)
            init_image = image
            init_time = time.time()
        else:
            _, image = cap.read()
            image = cv2.cvtColor(image,
                                 cv2.COLOR_BGR2GRAY)
            subtract = np.abs((init_image - image) / 255)
            count = np.count_nonzero(subtract > pixel_threshold)
            result_data.append(count)
            current_time = time.time()
            wait_interval = time_interval - (current_time - init_time)
            init_image=image
            init_time = time.time()
            time.sleep(wait_interval)
    # quit capturing
    cap.release()
    cv2.destroyAllWindows()
    return result_data


ans = Image_subtraction(time_interval, images)
plt.plot(ans)
