import numpy as np
from PIL import Image
from typing import Any


def ft_load(path: str) -> np.ndarray[(Any, Any, 3), np.int_]:
    """
    Function that loads an image from the path given as parameter,
    prints its shape and pixels content in rgb format.

    Note that jpg and jpeg are the only filetypes supported.

    @param path: path to image
    @return np_pixel_data: numpy ndarray containing image pixel data in rgb
    format.
    """

    try:
        img = Image.open(path)
        img.verify() # check for corruptions
        img = Image.open(path)
    except Exception as err:
        raise AssertionError("bad file")

    assert img.format in ["JPG", "JPEG"], "image format not supported"

    size = img.size

    shape = (size[0], size[1], 3)

    np_pixel_data = np.array(img)

    print(f"The shape of the image is : {shape}")

    return np_pixel_data
