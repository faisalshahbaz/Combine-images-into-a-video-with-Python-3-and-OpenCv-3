import cv2
import os
from os.path import isfile, join

dir_path = "images/"
ext = "jpg"

images = []
files = [f for f in os.listdir(dir_path) if isfile(join(dir_path, f))]
files.sort(key=lambda x: int(x[5:-4]))
for i in range(len(files)):
    filename = dir_path + files[i]
    img = cv2.imread(filename)
    cv2.imshow('video',img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

cv2.destroyAllWindows()



# import time
# start_time = time.time()

# #
# # Perform lots of computations.
# #
# time.sleep(4)
# elapsed_time_secs = time.time() - start_time


# print(int(elapsed_time_secs))
