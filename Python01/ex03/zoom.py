from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    Program that zooms into a portion of an image.
    """
    try:
        np_image_data = ft_load("../animal.jpeg")
    except AssertionError as err:
        print(f"AssertionError: {err.args[0]}")
        return

    print(np_image_data)

    np_zoomed = np_image_data[100:500, 450:850, 0:1]
    print(f"New shape after slicing: {np_zoomed.shape}")
    print(np_zoomed)

    plt.imshow(np_zoomed, cmap=plt.get_cmap('gray'))
    plt.show()


if __name__ == "__main__":
    main()
