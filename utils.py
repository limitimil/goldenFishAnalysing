import cv2
from IPython import Image

def excerption(left, right, up, down, x):
    h, w, _ = x.shape
    assert(left < right)
    assert(up < down)
    return x[up: down, left: right]
def myShow(cv2img):
    cv2.imwrite("./tmp.png", cv2img)
    return Image(filename='tmp.png')

