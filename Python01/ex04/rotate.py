from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """
    Program that zooms into a portion of an image, and then rotates it 90
    clockwise.
    """
    try:
        np_image_data = ft_load("../animal.jpeg")
    except AssertionError as err:
        print(f"AssertionError: {err.args[0]}")
        return

    np_zoomed = np_image_data[100:500, 450:850, 0:1]
    print(f"The shape of the image is : {np_zoomed.shape}")
    print(np_zoomed)

    np_transposed = (np.array([[row[i][0] for row in np_zoomed] for i in
                     range(len(np_zoomed))]))

    print(f"New shape after Transpose : {np_transposed.shape}")
    print(np_transposed)

    plt.imshow(np_transposed, cmap=plt.get_cmap('gray'))
    plt.show()


if __name__ == "__main__":
    main()
