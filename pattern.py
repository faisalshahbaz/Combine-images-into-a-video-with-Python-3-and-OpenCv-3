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



# image_path = os.path.join(dir_path, images[0])
#
# frame = cv2.imread(image_path)
# cv2.imshow('video',frame)
# height, width, channels = frame.shape

# for image in images:
#
#     image_path = os.path.join(dir_path, image)
#     frame = cv2.imread(image_path)
#
#     cv2.imshow('video',frame)
#     if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
#         break
#
# cv2.destroyAllWindows()

# vidcap = cv2.VideoCapture('video.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("images/frame%d.jpg" % count, image)     # save frame as JPEG file
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1