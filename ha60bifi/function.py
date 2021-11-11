import numpy as np
import matplotlib.pyplot as plt
#from ipywidgets import interact, fixed
from PIL import Image


def imshow(X, resize=None):
    """[Changes the shape of the image X to the desired shape (width, height)]

    Args:
        X ([Array]): [Array that will be converted to Pillow Image]
        resize ([2-tuple], optional): [New (width, height) of the image]. Defaults to None.
    """

    img = Image.fromarray(X, 'RGB')

    if resize!=None:
        resizedImg = img.resize(resize)
    else:
        resizedImg = img

    plt.imshow(resizedImg)
    plt.tight_layout()

    pass